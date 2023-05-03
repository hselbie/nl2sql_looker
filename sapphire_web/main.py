# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, send_from_directory
from flask import jsonify
from flask import request
 
from urllib.parse import urlencode

import glob
import json
import os

from absl import app
# from google.cloud.aiplatform.private_preview import language_models
from vertexai.preview.language_models import TextEmbeddingModel

from sapphire_llm.looker_dashboard_index import LookerDashboardIndex
from sapphire_llm import looker_helper
from sapphire_llm import prompt_helper
from sapphire_llm.vertex_llm import VertexEmbeddings
from flask_cors import CORS

INDEX_PATH='.chroma/index'
REQUESTS_PER_MINUTE = 15


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_url_path='', static_folder='../sapphire_frontend/build')
CORS(app)


files = glob.glob("lookml_updates/*.lookml")
reports = looker_helper.get_lookml_dashboard_descriptions(files)
for r in reports:
  print(r)

embedding_model = TextEmbeddingModel.from_pretrained("google/textembedding-gecko@001")

# embedding = VertexEmbeddings(language_models.TextEmbeddingModel(), requests_per_minute=REQUESTS_PER_MINUTE)
embedding = VertexEmbeddings(embedding_model, requests_per_minute=REQUESTS_PER_MINUTE)
looker_index = LookerDashboardIndex(INDEX_PATH, text_items=reports, embedding=embedding)

# web UI endpoint
@app.route('/ui', methods = ['GET'], defaults={'path': '/ui'})
def ui_route(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/query', methods = ['POST', 'GET'])
def query():
  #question = request.args.get("question")
  request_json = request.get_json()
  question = request_json["question"]
  entities = request_json["entities"]
  report_title_match = looker_index.query_index(question)[0]
  print("%%%%%%%%% report: ", report_title_match, " request entities: ", entities)
  error_msg = ""
  if entities:
    try:
      #question_entities = prompt_helper.entity_extraction(question, model="text-unicorn-001")
      question_entities = prompt_helper.entity_extraction(question, model="text-bison-001")
      question_entity_keys = list(filter(lambda x: question_entities[x] != '' and question_entities[x] != [], question_entities))
      print("**** @@@@@@@ question_entities: *****", question_entities)
      keys = list(filter(lambda x: entities[x] != '' and entities[x] != [], entities))
      filtered_entities = {key: entities[key] for key in keys}
      for key in question_entity_keys:
        filtered_entities[key] = question_entities[key]
    except:
      error_msg = "The entity extraction service had a temporary request error, please retry[1]"
      return jsonify({'results': '', 'llm_text': error_msg, 'entities': entities, 'looker_url': ''})

    if "cases" in report_title_match.lower() and filtered_entities['Year'] == '':
      filtered_entities['Year'] = 'this year'
    try:
      results, dashboard_id, header = looker_helper.get_query_results_with_filter(report_title_match, filtered_entities)
      print("$$$$$$$$$$ filtered entities: ", filtered_entities)

      # Use different prompts for different "intents".
      if "orders" in report_title_match.lower():
        answer = prompt_helper.summarize_response(results)
      elif "products" in report_title_match.lower():
        answer = prompt_helper.answer_question(question, header, results)
      elif "time" in report_title_match.lower():
        answer = prompt_helper.summarize_on_time_results(results, header)
      elif "news" in report_title_match.lower():
        answer = prompt_helper.summarize_news_results(results, header)
      elif "open cases" in report_title_match.lower():
        answer = prompt_helper.summarize_response(results, header)
      else:
        answer = prompt_helper.answer_question(question, header, results)

      looker_url = looker_helper.generate_looker_url(dashboard_id, urlencode(filtered_entities))
    except:
      print("error with report: ", report_title_match)
      return jsonify({'results': '', 'llm_text': 'There was an error with the dashboard: ' + report_title_match, 'entities': entities, 'looker_url': ''})
  else:
    try:
      question_entities = prompt_helper.entity_extraction(question, model="text-bison-001")
    except:
      error_msg = "The entity extraction service had a temporary request error, please retry[2]"
      return jsonify({'results': '', 'llm_text': error_msg, 'entities': entities, 'looker_url': ''})

    try:
      print("@@@@@@@ question_entities: ", question_entities)
      keys = list(filter(lambda x: question_entities[x] != '' and question_entities[x] != [], question_entities))
      filtered_entities = {key: question_entities[key] for key in keys}
      print("@@@@@@@ filtered question_entities: ", filtered_entities)
      if len(keys) > 0:
        results, dashboard_id, header = looker_helper.get_query_results_with_filter(report_title_match, filtered_entities)
        looker_url = looker_helper.generate_looker_url(dashboard_id, urlencode(filtered_entities))
      else:
        results, dashboard_id, header = looker_helper.get_query_results(report_title_match)
        looker_url = looker_helper.generate_looker_url(dashboard_id)
      answer = prompt_helper.answer_question(question, header, results)
      # answer = answer.split(".")[0]
      answer_entities = prompt_helper.entity_extraction(answer, model="text-bison-001")
      print("!@!@!@!@!@!", answer_entities)
      keys = list(filter(lambda x: answer_entities[x] != '' and answer_entities[x] != [], answer_entities))
      entities = {key: answer_entities[key] for key in keys}
    except:
      print("error with report: ", report_title_match)
      return jsonify({'results': '', 'llm_text': 'There was an error with the dashboard: ' + report_title_match, 'entities': entities, 'looker_url': ''})

  print("^^^^^^^^^^^", entities)
  entities['Product'] = ''
  return jsonify({'results': results, 'llm_text': answer, 'entities': entities, 'looker_url': looker_url})


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/test', methods = ['POST', 'GET'])
def test():
  question = "Which customer had the top average sales this year?"
  report_title_match = looker_index.query_index(question)[0]
  table_str = looker_helper.get_companies(report_title_match)
  items = table_str.strip().split('\n')
  print(items)
  return jsonify({'results': items, 'llm_text': 'test'})
 
# main driver function
if __name__ == '__main__':
 
  # run() method of Flask class runs the application
  # on the local development server.
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)

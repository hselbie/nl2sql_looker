# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, send_from_directory
from flask import jsonify
from flask import request
 

import glob
import json
import os

from absl import app
from google.cloud.aiplatform.private_preview import language_models
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


files = glob.glob("lookml/*.lookml")
reports = looker_helper.get_lookml_dashboard_descriptions(files)

embedding = VertexEmbeddings(language_models.TextEmbeddingModel(), requests_per_minute=REQUESTS_PER_MINUTE)
looker_index = LookerDashboardIndex(INDEX_PATH, text_items=reports, embedding=embedding)

# web UI endpoint
@app.route('/ui', methods = ['GET'], defaults={'path': '/ui'})
def ui_route(path):
    return send_from_directory(app.static_folder, 'index.html')


entity_stack = []

@app.route('/query', methods = ['POST', 'GET'])
def query():
  question = request.args.get("question")
  report_title_match = looker_index.query_index(question)[0]
  print(report_title_match)
  entities = {}
  results, dashboard_id = looker_helper.get_query_results(report_title_match)
  looker_url = looker_helper.generate_looker_url(dashboard_id)
  answer = prompt_helper.answer_question(question, results)
  answer = answer.split(".")[0]
  entities = prompt_helper.entity_extraction(answer)
  res = list(filter(lambda x: entities[x] != '', entities))
  key = res[0]
  #value = entities[key]
  print(entities)
  entity_stack.append(entities)

  return jsonify({'results': results, 'llm_text': answer, 'entities': entity_stack, 'looker_url': looker_url})


@app.route('/no_op', methods = ['POST', 'GET'])
def no_op():
  question = request.args.get("question")
  report_title_match = looker_index.query_index(question)[0]
  print(report_title_match)
  entities = {}
  looker_url = ''
  answer = ''
  if entity_stack:
    entities = entity_stack.pop()
    res = list(filter(lambda x: entities[x] != '', entities))
    key = res[0]
    value = entities[key]
    results = looker_helper.get_query_results_with_filter(report_title_match, key, value)

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

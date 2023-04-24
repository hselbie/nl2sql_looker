# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
 

import glob

from absl import app
from google.cloud.aiplatform.private_preview import language_models
from sapphire_llm.looker_dashboard_index import LookerDashboardIndex
from sapphire_llm import looker_helper
from sapphire_llm import prompt_helper
from sapphire_llm.vertex_llm import VertexEmbeddings

INDEX_PATH='.chroma/index'
REQUESTS_PER_MINUTE = 15

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 

files = glob.glob("lookml/*.lookml")
reports = looker_helper.get_lookml_dashboard_descriptions(files)
print(reports)

#embedding = VertexEmbeddings(language_models.TextEmbeddingModel(), requests_per_minute=REQUESTS_PER_MINUTE)
#looker_index = LookerDashboardIndex(INDEX_PATH, text_items=reports, embedding=embedding)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
  #question = "Which customer had the top average sales this year?"
  #report_title_match = looker_index.query_index(question)[0]
  #table_str = looker_helper.get_companies(report_title_match)
  return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
  # run() method of Flask class runs the application
  # on the local development server.
  app.run()

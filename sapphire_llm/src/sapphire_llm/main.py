"""Main test driver app for simulating the Sapphire demo story board."""

from collections.abc import Sequence
import glob

from absl import app
from google.cloud.aiplatform.private_preview import language_models
from sapphire_llm.looker_dashboard_index import LookerDashboardIndex
from sapphire_llm import looker_helper
from sapphire_llm import prompt_helper
from sapphire_llm.vertex_llm import VertexEmbeddings

INDEX_PATH='.chroma/index'
REQUESTS_PER_MINUTE = 15


def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  
  # read all files from directory with glob
  files = glob.glob("lookml/*.lookml")
  reports = looker_helper.get_lookml_dashboard_descriptions(files)

  embedding = VertexEmbeddings(language_models.TextEmbeddingModel(), requests_per_minute=REQUESTS_PER_MINUTE)
  looker_index = LookerDashboardIndex(INDEX_PATH, text_items=reports, embedding=embedding)

  question = "Which customer had the top average sales this year?"
  report_title_match = looker_index.query_index(question)[0]
  table_str = looker_helper.get_companies(report_title_match)

  prompt_response = prompt_helper.get_top_item(question, table_str)
  selected_company = prompt_helper.get_selected_company(prompt_response)
  print(prompt_response)
  print(selected_company)


  print("*" * 80)
  question = "What are the Total Cases Created?"
  report_title_match = looker_index.query_index(question, k=3)[0]
  looker_helper.get_open_cases(report_title_match, selected_company)

  print("*" * 80)
  question = "What are the top selling products?"
  report_title_match = looker_index.query_index(question, k=3)[0]
  results = looker_helper.get_query_results(report_title_match)
  print(results)

if __name__ == "__main__":
  app.run(main)

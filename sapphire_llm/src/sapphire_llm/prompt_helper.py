"""Helper LLM Prompt functions."""
import json
from google.cloud.aiplatform.private_preview import language_models
from sapphire_llm.vertex_llm import VertexLLM

model = language_models.TextGenerationModel.from_pretrained('text-bison-001')

vertex_llm = VertexLLM(
  model,
  max_output_tokens=2048,
  temperature=0.1,
  top_p=0.8,
  top_k=40
).model


def entity_extraction(sentence):
  prompt_template = """

Perform NER on the following sentence and only list entities that were given in the sentence. Use the following definitions for the entities to extract:
Year and Currency and Region and Sales Org and Distribution Channel and Product

1. YEAR: The year of the report
2. CURRENCY: The currency with a default of USD
3. REGION: The country, such as Canada, USA, Germany, Japan, etc.
4. SALES ORG: The sales, such as Canada sales org, Germany sales org, US East sales org, etc.
5. DISTRIBUTION CHANNEL: The distribution channel, such as Digital Sales, Retail Sales, Wholesale Sales, etc.
6. DIVISION: The division, such as packaged goods, electronics, perishables, etc.
7. PRODUCT: The product being sold, such as body scrub, laptop, pure fresh juice, etc.
8. COMPANY: The name of the company, such as Standard Retail, Tachinome Stores, Tirgil Canary, etc.

OUTPUT FORMAT:
{{'year': <the year>, 'currency': <the currency>, 'region': [The list of regions mentioned],
'sales_org': [The list of sales orgs mentioned], 'distribution_channel': [The list of distribution channels mentioned],
'division': [The list of divisions mentioned], 'product': [The list of products mentioned],
'Customer': <the company>}}

SENTENCE
{}
  """

  assembled_prompt = prompt_template.format(sentence)
  result_str = str(vertex_llm.predict(assembled_prompt))
  json_result = json.loads(result_str.replace('\'', '\"'))
  return json_result
  

def answer_question(question, table_str):
  prompt_template = f"""
  {question} based on the following information:
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response


def get_top_item(question, table_str):
  prompt_template = f"""
  {question} based on the following information:
  {table_str}
  """

  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response

def get_selected_company(prompt_response):
  prompt_template = """
Perform NER on the following sentence and only extract the name of the company given in the sentence. Use the following definition to extract the Company:

1. Company: The name of the company

OUTPUT FORMAT:
{{'Company': <the company>}}

SENTENCE
{}

"""

  assembled_prompt = prompt_template.format(prompt_response)
  response = str(vertex_llm.predict(assembled_prompt)).replace("'", "\"")

  selected_company = json.loads(response)['Company']
  return selected_company


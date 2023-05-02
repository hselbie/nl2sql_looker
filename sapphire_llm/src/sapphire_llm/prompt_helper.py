"""Helper LLM Prompt functions."""
import json
from google.cloud.aiplatform.private_preview import language_models
from sapphire_llm.vertex_llm import VertexLLM

model = language_models.TextGenerationModel.from_pretrained('text-bison-001')
#model = language_models.TextGenerationModel.from_pretrained('text-unicorn-001')

"""
vertex_llm = VertexLLM(
  model,
  max_output_tokens=2048,
  temperature=0.1,
  top_p=0.8,
  top_k=40
).model
"""

# TODO(agravat@): Change the reference to this model.
vertex_llm = VertexLLM(
  model=model,
  max_output_tokens=1024,
  temperature=0,
  top_p=0.2,
  top_k=40
)

def entity_extraction(sentence, model: str = "text-bison-001"):
  prompt_template = """

Perform NER on the following sentence and only list entities that were given in the sentence. Use the following definitions for the entities to extract:
Year and Currency and Region and Sales Org and Distribution Channel and Product and Customer. Set the default value for the currency if the value is null. 
If any of the other values are null then set them equal to empty string.  If any value is an empty list then set them equal to empty string.

1. YEAR: The year of the report
2. CURRENCY: The currency, the default value is USD
3. REGION: The country, such as Canada, USA, Germany, Japan, etc.
4. SALES ORG: The sales, such as Canada sales org, Germany sales org, US East sales org, etc.
5. DISTRIBUTION CHANNEL: The distribution channel, such as Digital Sales, Retail Sales, Wholesale Sales, etc.
6. DIVISION: The division, such as packaged goods, electronics, perishables, etc.
7. PRODUCT: The product being sold, such as body scrub, laptop, pure fresh juice, etc.
8. CUSTOMER: The name of the customer, such as Standard Retail, Tachinome Stores, Tirgil Canary, etc.

JSON OUTPUT FORMAT:
{{'Year': <the year>, 'Currency': 'USD', 'Region': [The list of regions mentioned],
'Sales Org': [The list of sales orgs mentioned], 'Distribution Channel': [The list of distribution channels mentioned],
'Division': [The list of divisions mentioned], 'Product': [The list of products mentioned],
'Customer': <the company>}}

SENTENCE
{}
  """

  assembled_prompt = prompt_template.format(sentence)
  result_str = str(vertex_llm.predict(assembled_prompt, model))
  print("prompt result entity extraction: ", result_str)
  try:
    if "```json" in result_str:
      json_result = json.loads(result_str.split("```json")[1].replace("\n","").split("```")[0].strip().replace("'", "\""))
    elif "```" in result_str:
      json_result = json.loads(result_str.split("```")[1].strip().replace("'", "\""))
    else:
      json_result = json.loads(result_str.replace('\'', '\"'))
  except:
    json_result = {}
  return json_result
  

def answer_question(question, header, table_str):
  prompt_template = f"""
  {question}
  {header}
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response

def summarize_response(table_str):
  prompt_template = f"""
  Summarize the following information:
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response

def summarize_product_sales_results(table_str):
  prompt_template = f"""
  Summarize the following products sales results:
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  print(prompt_response)
  return prompt_response

def summarize_news_results(table_results, header):
  
  prompt_template = f"""
  Summarize the trend of the news articles by month:
  {header}
  {table_results}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  print(prompt_response)
  return prompt_response

def summarize_on_time_results(table_results, header):
  
  prompt_template = f"""
  Summarize the following on time delivery results:
  {header}
  {table_results}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  print(prompt_response)
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


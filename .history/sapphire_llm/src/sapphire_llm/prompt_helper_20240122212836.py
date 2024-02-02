"""Helper LLM Prompt functions."""
import json
# from google.cloud.aiplatform.private_preview import language_models
from vertexai.preview.language_models import TextGenerationModel
from sapphire_llm.vertex_llm import VertexLLM
from config import variables

model = TextGenerationModel.from_pretrained('text-bison@001')
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
  temperature=0.0,
  top_p=0.2,
  top_k=1040
)


def _clean_response(response: str) -> str:
  if response.startswith('> '):
    return response.replace('> ', '', 1)
  return response

def entity_extraction(sentence, model: str = "text-bison@001"):
  prompt_template = """Perform entity extraction on the question below and only list entities that were given in the question. Use the following definitions for the entities to extract and only output the json object:
  
1. YEAR: The year of the report, the current year is 2023.
2. CURRENCY: The currency, the default value is USD
3. REGION: The country, such as Canada, USA, Germany, Japan, etc.
4. PRODUCT: The name of product being sold, such as body scrub, laptop, pure fresh juice, etc.
5. CUSTOMER: The name of the customer, such as Standard Retail, Tachinome Stores, Tirgil Canary, etc.

JSON OUTPUT FORMAT:
{{'Year': <the year>, 'Currency': 'USD', 'Region': <The region mentioned>, 'Product': <The name of the product>,
'Customer': <the customer>}}

EXAMPLES:
Question: Who is my top customer this year?
Answer: ```json{{'Year': 2023, 'Currency': 'USD', 'Region': '', 'Product': '', 'Customer': ''}}```

Question: What was Standard Retails monthly sales this year?
Answer: ```json{{'Year': 2023, 'Currency': 'USD', 'Region': '', 'Product': '', 'Customer': 'Standard Retail'}}```

Question: What is our current monthly sales volume?
Answer: ```json{{'Year': 2023, 'Currency': 'USD', 'Region': '', 'Product': '', 'Customer': ''}}```

Now answer the following question:
Question: {}
Answer:

  """

  assembled_prompt = prompt_template.format(sentence)
  print(assembled_prompt)
  result_str = str(vertex_llm.predict(assembled_prompt, model))
  result_str = result_str.replace('null', '')
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
  return _clean_response(prompt_response)

def summarize_stock_in_hand(table_str, header):
  prompt_template = f"""
  Who are the top vendors and products:
  {header}
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response

def summarize_delivery_performance(table_str, header):
  prompt_template = f"""
  Provide a short summary for the vendor delivery performance using the following information taking into account changes over time, and bias towards most recent data:
  {header}
  {table_str}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  return prompt_response

def summarize_response(table_str, header):
  prompt_template = f"""
  Summarize the following information:
  {header}
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
  return _clean_response(prompt_response)

def summarize_trend(table_results, header):
  
  prompt_template = f"""
  Summarize the trend for the following information:
  {header}
  {table_results}
  """
  print(prompt_template)
  prompt_response = str(vertex_llm.predict(prompt_template))
  print(prompt_response)
  return _clean_response(prompt_response)

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


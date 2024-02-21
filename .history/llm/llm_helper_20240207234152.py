import vertexai
from config import variables as var 
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
)
from llm import process_lkml
import datetime 

# Set the project and location

PROJECT_ID = var.var["project_id"]  # @param {type:"string"}
LOCATION_ID = var.var["region"]  # @param {type:"string"}

vertexai.init(project=PROJECT_ID, location=LOCATION_ID)

class VertexLLM:
  def __init__(self, model_name: str, max_output_tokens: int, temperature: float, top_p: float, top_k: int):
    self.model_name = model_name
    self.max_output_tokens = max_output_tokens
    self.temperature = temperature
    self.top_p = top_p
    self.top_k = top_k

  def predict(self, prompt: str) -> str:
    """Executes a prediction request to the Vertex AI LLM model.
    Args:
      prompt: The prompt to send to the model.
    Returns:
      The prediction response from the model.
    """
    model = GenerativeModel(self.model_name)
    modelConfig = GenerationConfig(
      temperature=self.temperature,
      top_p=self.top_p,
      top_k=self.top_k,
      candidate_count=1,
      max_output_tokens=self.max_output_tokens,
  )
    response = model.generate_content(
        prompt,
        generation_config=modelConfig,
    )
    return response.text

if __name__ == "__main__":
  test = VertexLLM(model_name="gemini-pro", max_output_tokens=100, temperature=0.7, top_p=0.9, top_k=3)

  with open("lookml/descriptions.txt", "r") as f:
    lookml_data = f.read()
  query = 'what is my revenue calculated by total sale price - gross margin for products sold in the last 28 days?' 
  today = datetime.datetime.now().strftime("%Y-%m-%d")

  intent = f'''
  identify the break out the semantic meaning of the question {query}'''
  question_intent = test.predict(intent)
  print(question_intent)

  primer = f'''  
  You are a database expert at selecting a series of database fields based on their relevance to a query.
    For this provided intent {question_intent}, and for this provided query {query}, choose what fields are most likely to be relevant
    from these fields {lookml_data} only.
    Only mention the fields that are relevant to the description-keywords. 
    Mention multiple field name if applicable. The field list is as follows: {lookml_data}
    if the field has a field-type of 'time' then add it to the timeframe section of the response. 
  return the response as a json object in the following format:
    For example: 
    Example Query 1: "what are my top-selling products last year"
    Example Response 1:{{
    "intent": "identify_top_performers",
    "entities": {{
      "fields": [
        "products.name",
        "order_items.total_sale_price",
        ]
      "timeframe": {{
        "field": "order_items.created_date",
        "period": "year",
        "duration": 1,
        "reference": "last" 
      }}
    }}
  }}

  Example Query 2: "what are my high value geographies for my top 5 selling products?"
  Example Response 2:{{
    "intent": "identify top markets",
    "entities": {{
      "fields": [
        "users.state",
        "order_items.total_sale_price"
        ]
      "timeframe": {{
        "field": "order_items.created_date",
        "period": "days",
        "duration": 28,
        "reference": "last"
      }}
    }}
  }}
    

  If a time component is referenced in the prompt, use the current date {today} and perform the appropriate calculations to return the initial date.
  For example 
  if today's date is '2024-1-24', and the prompt contains the description 'last year' the value should return '2023-1-24'. 
  if today's date is '2024-1-24', and the prompt contains the description 'last 6 months' the value should return '2023-7-24'. 
  if today's date is '2024-1-24', and the prompt contains the description 'in the last 28 days' the value should return '2023-12-29'. 
  if today's date is '2024-1-24', and the prompt contains the description 'last week' the value should return '2024-1-17'. 
  '''
  
  print(test.predict(primer))
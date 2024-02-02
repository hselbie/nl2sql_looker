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
  query = 'what are my top selling products in the last year?' 
  today = datetime.datetime.now().strftime("%Y-%m-%d")

  intent = f'''
  identify the break out the semantic meaning of the question {query} 
  return the response as a json object in the following format:
  For example: 
  "what are my top-selling products last year"
  {{
  "intent": "identify_top_performers",
  "entities": {{
    "owner": "my",
    "metric": "top-selling",
    "products": true,  
    "timeframe": {{
      "period": "year",
      "reference": "last" 
    }}
  }},
  "implications": [
    "inventory_management",
    "trend_identification",
    "performance_evaluation"
  ]
}}
"what products do i need to order based on sales numbers in the last 28 days"
{{
  "intent": "restock_decision",
  "entities": {{
    "products": true,
    "decision_criteria": "sales_numbers",
    "timeframe": {{
      "period": "days",
      "duration": 28,
      "reference": "last"
    }}
  }},
  "implications": [
    "inventory_management",
    "demand_forecasting"
  ]
}}'''

  primer = f'''  
  You are a database expert at selecting a series of database fields based on their relevance to a query.
    For this provided question intent{intent}, and for this provided query {query}, choose what fields are most likely to be relevant.
    Only mention the field name from the following json string and their description-keywords. 
    Mention multiple field name if applicable. The json string is as follows: {lookml_data}

  If a time component is referenced in the prompt, use the current date {today} and perform the appropriate calculations to return the initial date.
  For example 
  if today's date is '2024-1-24', and the prompt contains the description 'last year' the value should return '2023-1-24'. 
  if today's date is '2024-1-24', and the prompt contains the description 'last 6 months' the value should return '2023-7-24'. 
  if today's date is '2024-1-24', and the prompt contains the description 'in the last 28 days' the value should return '2023-12-29'. 
  if today's date is '2024-1-24', and the prompt contains the description 'last week' the value should return '2024-1-17'. 
  '''
  
  print(test.predict(primer))
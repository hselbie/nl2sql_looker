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

  # with open("lookml/order_items.json", "r") as f:
    # lookml_data = json.load(f)
  lookml_files = ['lookml/order_itemsII.lkml','lookml/products.lkml','lookml/inventory_items.lkml', 'lookml/distribution_centers.lkml']
  lookml_data = process_lkml.main(lookml_files=lookml_files)
  query = 'what are is my top selling products in the last year?' 
  today = datetime.datetime.now().strftime("%Y-%m-%d")

  primer = f'''  
  You are a database expert at selecting a series of fields from a json string based on their description.
    For this provided question {query}, choose what fields are most likely to be relevant.
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
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
  pass
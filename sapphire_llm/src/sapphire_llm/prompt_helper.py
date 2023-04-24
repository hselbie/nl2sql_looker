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


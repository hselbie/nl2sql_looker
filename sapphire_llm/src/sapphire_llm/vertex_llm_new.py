"""Vertex LLM API Wrapper module for text generation and embeddings."""

import time

# from google.cloud.aiplatform.private_preview import language_models
from vertexai.preview.language_models import TextGenerationModel
import vertexai

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

from langchain.embeddings.base import Embeddings
from langchain.llms.base import LLM

def rate_limit(max_per_minute):
  period = 60 / max_per_minute
  while True:
    before = time.time()
    yield
    after = time.time()
    elapsed = after - before
    sleep_time = max(0, period - elapsed)
    if sleep_time > 0:
      print(f'Sleeping {sleep_time:.1f} seconds')
      time.sleep(sleep_time)


class VertexEmbeddings(Embeddings):

  def __init__(self, model, *, requests_per_minute=15):
    self.model = model
    self.requests_per_minute = requests_per_minute

  def embed_documents(self, texts):
    limiter = rate_limit(self.requests_per_minute)
    results = []
    docs = list(texts)

    while docs:
      # Working in batches of 2 because the API apparently won't let
      # us send more than 2 documents per request to get embeddings.
      head, docs = docs[:2], docs[2:]
      chunk = self.model.get_embeddings(head)
      results.extend(chunk)
      next(limiter)

    return [r.values for r in results]

  def embed_query(self, text):
    single_result = self.embed_documents([text])
    return single_result[0]


class VertexLLM(LLM):

  # model: language_models.LanguageModel
  model: TextGenerationModel

  predict_kwargs: dict

  def __init__(self, model, **predict_kwargs):
    super().__init__(model=model, predict_kwargs=predict_kwargs)

  @property
  def _llm_type(self):
    return 'vertex'

  def _call(self, prompt, stop=None):
    #result = self.model.predict(prompt, **self.predict_kwargs)
    result = self.predict(prompt)
    return str(result)
  
  def predict(self, prompt: str, model_name: str = 'text-bison@001'):
    return self._predict_large_language_model_sample("cortex-demo-genai", 
                                                     model_name,
                                                     f'''{{"content": {prompt}}}''',
                                                    temperature=self.predict_kwargs['temperature'],
                                                    max_output_tokens=self.predict_kwargs['max_output_tokens'],
                                                    top_k=self.predict_kwargs['top_k'],
                                                    top_p=self.predict_kwargs['top_p'], 
                                                    location="us-central1")

  def _predict_large_language_model_sample(
    self,
    project_id: str,
    model_name: str,
    content: str,
    temperature: float,
    max_output_tokens: int,
    top_p: float,
    top_k: int,
    location: str = "us-central1",
    tuned_model_name: str = "",
  ):
    # The AI Platform services require regional API endpoints.
    # client_options = {"api_endpoint": api_endpoint}
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
      model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
        top_k=top_k,
        top_p=top_p,)
    return response.text


  @property
  def _identifying_params(self):
    return {}

# NOTE: Use staging to get 100qps max throughput for embedding indexing
# The embedding content is the same as production so you can use staging
# for indexing and production for querying if desired.
#language_models.TextEmbeddingModel._LLM_ENDPOINT_NAME = (
#  'projects/678515165750/locations/us-central1/endpoints/8156038716377268224')

"""
REQUESTS_PER_MINUTE = 15
#REQUESTS_PER_MINUTE = 6000

model = language_models.TextGenerationModel.from_pretrained('text-bison-001')
llm = VertexLLM(
  model,
  max_output_tokens=1024,
  temperature=0.1,
  top_p=0.8,
  top_k=40
)
embedding = VertexEmbeddings(language_models.TextEmbeddingModel(), requests_per_minute=REQUESTS_PER_MINUTE)

# llm

# Set up model instance for use later
vertex_llm = VertexLLM(model,max_output_tokens=1024).model
"""

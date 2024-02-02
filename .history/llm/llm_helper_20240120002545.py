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
    from vertexai.preview.language_models import TextGenerationModel

    model = TextGenerationModel.from_pretrained(self.model_name)

    response = model.predict(
        prompt=prompt,
        max_output_tokens=self.max_output_tokens,
        temperature=self.temperature,
        top_p=self.top_p,
        top_k=self.top_k,
    )

    return response.text

"""BQ Quuery Helper."""

from google.cloud import bigquery


class BQHelper:
  def __init__(self, project_id: str):
    self.client = bigquery.Client(project=project_id)

  def query(self, query_str: str):
    query_job = self.client.query(query_str)

    return query_job.result()

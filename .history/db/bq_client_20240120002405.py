import google.cloud import bigquery as bigquery

class BigQueryHelper:
  def __init__(self, project_id: str):
    self.project_id = project_id
    self.client = bigquery.Client(project=project_id)

  def query(self, sql_query: str) -> bigquery.QueryJob:
    """Executes a SQL query on BigQuery.

    Args:
      sql_query: The SQL query to execute.

    Returns:
      A BigQuery QueryJob object representing the query.
    """
    return self.client.query(sql_query)

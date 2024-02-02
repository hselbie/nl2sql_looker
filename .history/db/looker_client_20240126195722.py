import looker_sdk

class LookerClient:
    def __init__(self, ini_location: str):
        self.ini_location = ini_location

    def get_client(self):
        sdk =looker_sdk.init40(config_file=self.ini_location)
        return sdk

    def create_query_body(self, model: str, view: str, fields: list, filters: dict):
        body = looker_sdk.models.WriteQuery(
            model=model,
            view=view,
            fields=fields,
            filters=filters
        )
        return body

    def run_inline_query(self, query_body: dict, result_format: str):
        sdk = self.get_client()
        amended_query_body = self.create_query_body(model=query_body['model'], view=query_body['view'], fields=query_body['fields'], filters=query_body['filters'])
        result = sdk.run_inline_query(result_format=result_format, body=amended_query_body)
        return result

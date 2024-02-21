import looker_sdk
import json
class LookerClient:
    def __init__(self, ini_location: str):
        self.ini_location = ini_location

    def get_client(self):
        sdk =looker_sdk.init40(config_file=self.ini_location)
        return sdk


    def create_query_body(self, model: str, view: str, fields: list):
        body = looker_sdk.models.WriteQuery(
            model=model,
            view=view,
            fields=fields
        )
        return body

    def make_valid_json(self, query: str):
        while isinstance(query, str):
            try:
                query = json.loads(query)
            except json.decoder.JSONDecodeError as err:
                continue
        return query


    def run_inline_query(self, query_body: str, result_format: str):
        query_body = self.make_valid_json(query_body)
        sdk = self.get_client()
        filter_field = query_body['filter']['field']
        filter_time_period = query_body['filter']['period']
        filter_time_value = query_body['filter']['duration']
        filter_val = f'{filter_field}: {filter_time_value} {filter_time_period}'
        amended_query_body = self.create_query_body(
            model='intermediate_ecomm', 
            view='intermediate_example_ecommerce', 
            fields=query_body['entities']['fields'] 
            filters=filter_val
            )
        print(amended_query_body)
        result = sdk.run_inline_query(result_format=result_format, body=amended_query_body)
        return result

    def test(self):
        sdk = self.get_client()
        test_response = sdk.me()
        print(test_response)

if __name__ == "__main__":
    location ='/usr/local/google/home/hugoselbie/code_sample/py/ini/lags.ini'
    test = LookerClient(ini_location=location) 
    test.test()



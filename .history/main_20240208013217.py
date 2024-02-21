from llm.llm_helper import VertexLLM
from db.looker_client import LookerClient
import pandas as pd
import json

query = 'what are my top-selling products last year' 

vertex_query_engine = VertexLLM(model_name="gemini-pro", max_output_tokens=100, temperature=0.7, top_p=0.9, top_k=3)

with open("lookml/descriptions.txt", "r") as f:
    LOOKML_DATA = f.read()
ENTRY_QUERY = 'what is my revenue calculated by total sale price - gross margin for products sold in the last 28 days?' 
LOOKER_API_CREDENTIALS = '/usr/local/google/home/hugoselbie/code_sample/py/ini/lags.ini'

intent = f'''
identify the semantic meaning of the question {query}'''
question_intent = vertex_query_engine.predict(intent)
print(question_intent)

primer = f'''  
You are a database expert at selecting a series of database fields based on their relevance to a query.
For this provided intent {question_intent}, and for this provided query {query}, choose what fields are most likely to be relevant
from these fields {LOOKML_DATA}.
Only mention the fields that are relevant to the description-keywords. 
Mention multiple field name if applicable. The field list is as follows: {LOOKML_DATA}

Instructions:
Respond using this format only.
Adhere strictly to the provided schema. Fill in missing values with appropriate defaults (e.g., null, empty array, etc.) if the information is unavailable or cannot be determined.
Include an "error" field at the top level to indicate any issues with generating the required data.

You are an expert in writing JSON, Validate the response is in this format only, do not deviate from this json format
{{"intent": INTENT,
    "entities": {{
      "fields": [
        FIELDS
        ]
      "timeframe": {{
        "field": TIME_FIELD,
        "period": TIME_PERIOD,
        "duration": DURATION,
        "reference": "last" 
      }}
    }}
  }}


    Example Response 1:{{
    "intent": "identify_top_performers",
    "entities": {{
      "fields": [
        "products.name",
        "order_items.total_sale_price",
        ]
      "timeframe": {{
        "field": "order_items.created_date",
        "period": "year",
        "duration": 1,
        "reference": "last" 
      }}
    }}
  }}

  Example Query 2: "what are my high value geographies for my top 5 selling products?"
  Example Response 2:{{
    "intent": "identify top markets",
    "entities": {{
      "fields": [
        "users.state",
        "order_items.total_sale_price"
        ]
      "timeframe": {{
        "field": "order_items.created_date",
        "period": "days",
        "duration": 28,
        "reference": "last"
      }}
    }}
  }}

  Validate the response is in a json format and all curly brackets have a match
'''
looker = LookerClient(ini_location=LOOKER_API_CREDENTIALS)
query_metadata = vertex_query_engine.predict(primer)
while isinstance(query_metadata, str):
    try:
        print(query_metadata)
        query_metadata= json.loads(query_metadata)
    except json.decoder.JSONDecodeError as err:
        query_metadata = vertex_query_engine.predict(primer)
       

print(query_metadata)
x = looker.run_inline_query(query_body=query_metadata, result_format='json')
print(x)
x = json.loads(x)
df = pd.DataFrame(x)
print(df.head())
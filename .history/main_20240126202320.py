from llm import VertexLLM
from db import looker_client

vertex_query_engine = VertexLLM(model_name="gemini-pro", max_output_tokens=100, temperature=0.7, top_p=0.9, top_k=3)

with open("lookml/descriptions.txt", "r") as f:
    LOOKML_DATA = f.read()
ENTRY_QUERY = 'what is my revenue calculated by total sale price - gross margin for products sold in the last 28 days?' 
LOOKER_API_CREDENTIALS = '../../lags.ini'

intent = f'''
identify the break out the semantic meaning of the question {query}'''
question_intent = vertex_query_engine.predict(intent)
print(question_intent)

primer = f'''  
You are a database expert at selecting a series of database fields based on their relevance to a query.
For this provided intent {question_intent}, and for this provided query {query}, choose what fields are most likely to be relevant
from these fields {lookml_data}.
Only mention the fields that are relevant to the description-keywords. 
Mention multiple field name if applicable. The field list is as follows: {lookml_data}
return the response as a json object in the following format:
For example: 
Example Query 1: "what are my top-selling products last year"
Example Response 1:{{
"intent": "identify_top_performers",
"entities": {{
    "fields": [
    "products.product_name",
    "order_items.total_sale_price",
    "order_items.created
    ]
    "timeframe": {{
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
    "order_items.total_sale_price",
    "order_items.created
    ]"products": true,
    "timeframe": {{
    "period": "days",
    "duration": 28,
    "reference": "last"
    }}
    }}
}}
'''
looker = looker_client(ini_location='LOOKER_API_CREDENTIALS')
looker.run
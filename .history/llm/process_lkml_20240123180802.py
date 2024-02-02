import lkml
import pandas as pd
from llm import llm_helper

with open('lookml/order_itemsII.lkml') as f:
    lkml_file = lkml.load(f)

dims = lkml_file['views'][0]['dimensions']
# meas = lkml_file['views'][0]['measures']
# dim_groups = lkml_file['views'][0]['dimension_groups']

dim_df = pd.DataFrame(dims)
dim_df['view'] = 'order_items'
dict_list = [row._asdict() for row in dim_df.itertuples(index=False)]

for dict in dict_list:
    predictor = llm_helper.VertexLLM(model_name='gemini-pro', max_output_tokens=300, temperature=0.7, top_p=0.9, top_k=5)
    helper = '''
    1. A lookml object is taken from a table called 'order_items', this table has information about items that have been ordered from an 
    ecommerce website. 
    
    2. A single lookml object is represented as this dict in json format {dict}. 

    3. Write a description field for this object and only this object, extracting the values from the json keys. 
    Only list entities that were given in the dict. Ignore any values with "nan". 
    
    4. Ensure the result reads well and is grammatically correct and complete. 
    
    5. Only return the description text about the field referenced in the json.'''
    new_description = predictor.predict(helper)
    dict['description'] = new_description

    print(dict)







# meas_df = pd.DataFrame(meas)
# meas_df['view'] = 'order_items'
# dim_groups_df = pd.DataFrame(dim_groups)
# dim_groups_df['view'] = 'order_items'


# dim_df_ltd = dim_df[['name', 'description', 'view']]
# meas_df_ltd = meas_df[['name', 'description', 'view']]
# dim_groups_df_ltd = dim_groups_df[['name', 'description','view']]

# df = pd.concat([dim_df_ltd, meas_df_ltd, dim_groups_df_ltd], axis=0)

# df.to_json('lookml/order_items.json', orient='records')

# print(df.head())
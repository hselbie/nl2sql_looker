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
    predictor = llm_helper.VertexLLM(model_name='gemini-pro', max_output_tokens=300, temperature=0.2, top_p=0.9, top_k=5)
    helper = '''
    A LookML field can be a dimension, measure, or dimension group. 
    An example of a dimension is:
    dimension: user_id {
        description: "the id associated with a specific user"
        label: "User Id"
        type: number
        sql: ${TABLE}.user_id ;;
    }

    For the dimension above
    The object name is the name of the dimension located after the colon. 
    In the example above the object name is user_id. 

    The Label is the value of the label key in the json. 
    In the example above the label is User Id.

    The description is the value of the description key in the json. 
    In the example above the description is "the id associated with a specific user".

    An example of a dimension group is:
    dimension_group: returned {
        description: "order object returned date"
        type: time
        timeframes: [time, date, week, month, raw]
        sql: ${TABLE}.returned_at ;;
    }
    For the dimension group above
    The object name is the name of the dimension_group located after the colon. 
    In the example above the object name is returned. 

    The description is the value of the description key in the json. 
    In the example above the description is "order object returned date".

    The timeframes is the value of the timeframes key in the json. 
    In the example above the timeframes is [time, date, week, month, raw].

    An example of a measure is:
    measure: count {
        label: "count order items"
        description: "count of order items"
        type: count
        drill_fields: [id, user.first_name, user.last_name]
    }

    For the measure above
    The object name is the name of the measure located after the colon. 
    In the example above the object name is count. 

    The Label is the value of the label key in the json. 
    In the example above the label is count order items.

    The description is the value of the description key in the json. 
    In the example above the description is "count of order items".

    1. A single lookml object is represented as this dict in json format {dict}. The name of the object is represented by 
    the key `label` and `name` in the json. If both fields are populated use the label field in the description and if not 
    use the name field. Ignore the field `view` in the description. 

    2. Write a description field for this object and only this object, extracting the values from the json keys. 
    Only list entities that were given in the dict. Ignore any values with "nan". 
    
    3. Ensure the result reads well and is grammatically correct and complete. 
    
    4. Only return the description text about the field referenced in the json.'''
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

import lkml
import pandas as pd
import llm_helper

with open('lookml/order_itemsII.lkml') as f:
    lkml_file = lkml.load(f)

dims = lkml_file['views'][0]['dimensions']
meas = lkml_file['views'][0]['measures']
dim_groups = lkml_file['views'][0]['dimension_groups']

dim_df = pd.DataFrame(dims)
dim_df['view'] = 'order_items'
meas_df = pd.DataFrame(meas)
meas_df['view'] = 'order_items'
dim_groups_df = pd.DataFrame(dim_groups)
dim_groups_df['view'] = 'order_items'


dim_df_ltd = dim_df[['name', 'description', 'view']]
meas_df_ltd = meas_df[['name', 'description', 'view']]
dim_groups_df_ltd = dim_groups_df[['name', 'description','view']]

df = pd.concat([dim_df_ltd, meas_df_ltd, dim_groups_df_ltd], axis=0)

df.to_json('lookml/order_items.json', orient='records')

print(df.head())

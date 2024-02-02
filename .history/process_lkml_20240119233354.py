import lkml
import pandas as pd

with open('lookml/order_items.lkml') as f:
    lkml_file = lkml.load(f)

dims = lkml_file['views'][0]['dimensions']
meas = lkml_file['views'][0]['measures']
dim_groups = lkml_file['views'][0]['dimension_groups']

dim_df = pd.DataFrame(dims)
meas_df = pd.DataFrame(meas)
dim_groups_df = pd.DataFrame(dim_groups)

dim_df_ltd = dim_df[['name', 'description']]
meas_df_ltd = meas_df[['name', 'description']]
dim_groups_df_ltd = dim_groups_df[['name', 'description']]

df = pd.concat([dim_df_ltd, meas_df_ltd, dim_groups_df_ltd], axis=0)
print(df.head())

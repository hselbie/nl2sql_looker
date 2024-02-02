import lkml
import pandas as pd
from llm import llm_helper
import yaml

def parse_lookml(file_path):
    """
    Parses the LookML file and extracts object names.

    Args:
    file_path (str): Path to the LookML file.

    Returns:
    list: A list of LookML object names.
    """
    with open(file_path, 'r') as file:
        lookml_content = yaml.safe_load(file)
        # Assuming the structure is straightforward and all objects are top-level keys
        return list(lookml_content.keys())

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
    1. A single object is represented as a dict in json format {dict}. The name of the object is represented by 
    the key `label` and `name` in the json. If both fields are populated use the label field in the description and if not 
    use the name field. Ignore the field `view` in the description. 

    2. Write a description field for this object and only this object, extracting the values from the json keys. 
    Only list entities that were given in the dict. Ignore any values with "nan". 
    
    3. Ensure the result reads well and is grammatically correct and complete. 
    
    4. Only return the description text about the field referenced in the json.'''
    new_description = predictor.predict(helper)
    dict['description'] = new_description

if __name__ == '__main__':
    order_items = parse_lookml('lookml/order_itemsII.lkml'))


    print('done')
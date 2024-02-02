import lkml
import pandas as pd
from llm import llm_helper
import yaml
def read_lookml_file(file_path):
    """
    Reads the contents of a LookML file and returns it as a string.

    Args:
    file_path (str): The path to the LookML file.

    Returns:
    str: The content of the LookML file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {str(e)}"
# with open('lookml/order_itemsII.lkml') as f:
#     lkml_file = lkml.load(f)

# dims = lkml_file['views'][0]['dimensions']
# # meas = lkml_file['views'][0]['measures']
# # dim_groups = lkml_file['views'][0]['dimension_groups']

# dim_df = pd.DataFrame(dims)
# dim_df['view'] = 'order_items'
# dict_list = [row._asdict() for row in dim_df.itertuples(index=False)]

# for dict in dict_list:
#     predictor = llm_helper.VertexLLM(model_name='gemini-pro', max_output_tokens=300, temperature=0.2, top_p=0.9, top_k=5)
#     helper = '''
#     1. A single object is represented as a dict in json format {dict}. The name of the object is represented by 
#     the key `label` and `name` in the json. If both fields are populated use the label field in the description and if not 
#     use the name field. Ignore the field `view` in the description. 

#     2. Write a description field for this object and only this object, extracting the values from the json keys. 
#     Only list entities that were given in the dict. Ignore any values with "nan". 
    
#     3. Ensure the result reads well and is grammatically correct and complete. 
    
#     4. Only return the description text about the field referenced in the json.'''
#     new_description = predictor.predict(helper)
#     dict['description'] = new_description

if __name__ == '__main__':
    order_items = read_lookml_file('lookml/order_itemsII.lkml')


    print('done')
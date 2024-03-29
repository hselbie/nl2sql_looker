import lkml
import pandas as pd
from llm import llm_helper
import ast

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

def get_description(file_path):
    lookml_file = read_lookml_file(file_path)
    predictor = llm_helper.VertexLLM(model_name='gemini-pro-vision', max_output_tokens=2048, temperature=0.5, top_p=0.9, top_k=5)
    helper = f'''
    This is a lookml file. {lookml_file}
    write a description field for each lookml field object and return in a list of dictionaries  
    {{
        "view_name.field_name": "LookMLFieldName.LookMLViewName", 
        "description":{{DESCRIPTION}}, 
        "field_type": "LookML field type" 
        }}
    '''
    new_description = predictor.predict(helper)
    
    validator = f'''verify this is in the correct format for a python list of dictionaries
    {new_description}, if not amend the entry to ensure it is in the correct format, but do not change any of the data, make sure
    each list has a paired '[]', and each dictionary has a paired '{{}}'.
    return only the list of dictionaries in pure python code.
    '''

    validated_description = predictor.predict(validator)
    return new_description 

def main(lookml_files):
    key = []
    i = 0

    while i+1 < len(lookml_files):
        try:
            descriptions = get_description(lookml_files[i])
            listy = ast.literal_eval(descriptions)
            for elem in listy:
                key.append(elem)
            i = i + 1
            print(len(key))
            print(i)
        except Exception as e:
            print(e)
            continue
    return key

if __name__ == '__main__':
    lookml_files = ['lookml/order_itemsII.lkml','lookml/products.lkml','lookml/inventory_items.lkml', 'lookml/distribution_centers.lkml']
    key = main(lookml_files)
    with open('lookml/descriptions.txt', 'w') as f:
        for item in key:
            f.write("%s\n" % item)
    
    print(key)
    print(type(key))
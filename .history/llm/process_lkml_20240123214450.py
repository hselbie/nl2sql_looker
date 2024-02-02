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

def get_description(file_path):
    lookml_file = read_lookml_file(file_path)
    predictor = llm_helper.VertexLLM(model_name='gemini-pro', max_output_tokens=300, temperature=0.5, top_p=0.9, top_k=5)
    helper = f'''
    This is a lookml file. {lookml_file}
    write a description field for each lookml field object and return in a list of dictionaries  
    '''
    new_description = predictor.predict(helper)
    return new_description

if __name__ == '__main__':
    order_items = get_description('lookml/order_itemsII.lkml')


    print(order_items)
    print(type(order_items))
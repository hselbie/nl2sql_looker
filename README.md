# Natural Language to SQL Demo
This uses Looker and LookML as pass through to create a data dictionary augmenting data using LLM's to better match semantic queries and return a standardized body that can be easily accessed by the looker api.

It's undergoing active development.
## Pre-requisites
## to do
- create a virtual env `virtualenv venv`
- activate virtualenv: `source venv/bin/activate`
- install requirements: `pip install -r requirements.txt`
- add a looker.ini file to the config directory
- add an explore selector
- evaluate results against existing code generation model e.g. text2sql, codey, gemini, gpt4 etc.

## High Level
Using Looker to solve the existing NL to SQL problem that exists. 
In this process we can use LookML as an interstitial translation layer for asking natural language queries against
a SQL database. Typically some of the issues with this problem exist around making sure the appropriate columns are selected, which requires querying the schema of the database. 
In addition complicated joins and unnesting are often not created by existing fine tuned code based LLM's such as codey/gemini etc. 

This method steps.
- Take the existing LookML and create a data dictionary
- augment the datadictionary with context using an LLM
- Create a LLM prompt to select the question intent and output a standardized response in JSON format
- Use the json response to call Looker's robust api and return results.

The advantages of this method are:
1. Easy to create an augmented data dictionary from LLM scanning LookML
2. SQL generated is created by Looker to allow for complicated queries unnesting, joins etc. 
3. You can point this methods towards Dashboard filters, explores etc. 
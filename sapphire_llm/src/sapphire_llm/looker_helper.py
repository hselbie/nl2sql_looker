"""Lookml SDK Sapphire Helper functions."""

import yaml
import re
from looker_sdk import init40, models40
from sapphire_llm.bq_client import BQHelper

sdk = init40(config_file='/config/looker.ini')
bq_helper = BQHelper('cortex-demo-genai')


def human_format(num):
  num = float('{:.3g}'.format(num))
  magnitude = 0
  while  abs(num) >= 1000:
    magnitude += 1
    num /= 1000.0
  return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


def get_lookml_dashboard_descriptions(files):
  reports = []

  pattern = '<[^<]+?>'
  # for f in files:
  # print(f)
  for filename in files:
    with open(filename, 'r') as file:
      fulfillment = yaml.safe_load(file)
      try:
        if 'subtitle_text' in fulfillment[0]['elements'][0]:
          subtitle_text = re.sub(pattern, "", fulfillment[0]['elements'][0]['subtitle_text']).rstrip()
        else:
          subtitle_text = ''
        for i in range(len(fulfillment[0]['elements'])):
          element = fulfillment[0]['elements'][i]
          if 'title' in element:
            title = element['title'].rstrip()
            title_report = element['title'].replace(" ", "_").replace("%", "percent").replace("&", "and")
            # print(filename, title_report)

            if 'Untitled' not in title:
              # The filter attributes in the report.
              attributes = list(element['listen'].keys())
              if subtitle_text:
                # report = f'{title_report}: {subtitle_text} for {title} and the only information given is {attributes[0]} and {" and ".join(attributes[1:-1])}'
                report = f'{title_report}: {subtitle_text} for {title}'
              else:
                # report = f'{title_report}: {title} and the only information given is {attributes[0]} and {" and ".join(attributes[1:-1])}'
                report = f'{title_report}: {title}'
              # print("added: ", report)
              reports.append(report)

      except:
        pass

  return reports


def get_companies(report_title_match):
  elements = sdk.search_dashboard_elements(title=report_title_match)
  company_results = []
  report_title = ''
  for element in elements:
    if element.result_maker and int(element.dashboard_id) > 10:
      print("title: ", element.title) #, element.result_maker)
      report_title = element.title
      query_str = sdk.run_query(element.result_maker.query_id, result_format="sql")
      query_results = bq_helper.query(query_str)
      for row in query_results:
        if row[1] is not None:
          company_results.append((row[0], human_format(row[1])))
      break

  table_str = ''
  for i, company_result in enumerate(company_results):
    table_str += f'{i+1}. {report_title} for {company_result[0]} was {company_result[1]}\n'

  return table_str
  

def get_open_cases(report_title_match, selected_company):
  print(report_title_match, selected_company)
  elements = sdk.search_dashboard_elements(title=report_title_match)
  # print(elements)
  case_results = []
  for element in elements:
    filter_fields = element.result_maker.filterables[0].listen
    for field_element in filter_fields:
        if field_element.dashboard_filter_name == 'Account Name':
          altered_query = element.result_maker.query
          altered_query.client_id = None
          altered_query.id = None
          altered_query.filters = {field_element.field: selected_company}
          query_str = sdk.run_inline_query(body=altered_query, result_format="sql")
          query_str = sdk.run_query(element.result_maker.query_id, result_format="sql")
          query_results = bq_helper.query(query_str)
          for row in query_results:
            case_results.append(row)
          break
  print(case_results)


def get_query_results(report_title_match):
  elements = sdk.search_dashboard_elements(title=report_title_match)
  results = []
  for element in elements:
    if element.result_maker and int(element.dashboard_id) == 12:
      query_str = sdk.run_query(element.result_maker.query_id,result_format="sql")
      query_results = bq_helper.query(query_str)
      for row in query_results:
        results.append(row[0])
      break

  return results

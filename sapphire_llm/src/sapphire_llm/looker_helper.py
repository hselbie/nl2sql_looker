"""Lookml SDK Sapphire Helper functions."""

import os
import yaml
import re
from looker_sdk import init40, models40
from sapphire_llm.bq_client import BQHelper

if os.path.isfile('config/looker.ini'):
  sdk = init40(config_file='config/looker.ini')
else:
  sdk = init40(config_file='/config/looker.ini')
bq_helper = BQHelper('cortex-demo-genai')


def human_format(num):
  num = float('{:.3g}'.format(num))
  magnitude = 0
  while  abs(num) >= 1000:
    magnitude += 1
    num /= 1000.0
  return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


def generate_looker_url(dashboard_id: str, **kwargs) -> str:
  sso_body = models40.EmbedSsoParams(
      target_url=f"https://cortexqa.cloud.looker.com/dashboards/{dashboard_id}",
      session_length=15*60,
      force_logout_login=False,
      external_user_id="3",
      first_name="Adam",
      last_name="Dell",
      permissions=["access_data",
                            "see_lookml_dashboards",
                            "see_looks",
                            "see_user_dashboards",
                            "explore",
                            "create_table_calculations",
                            "create_custom_fields",
                            "can_create_forecast",
                            "save_content",
                            "create_public_looks",
                            "download_with_limit",
                            "download_without_limit",
                            "schedule_look_emails",
                            "schedule_external_look_emails",
                            "create_alerts",
                            "follow_alerts",
                            "send_to_s3",
                            "send_to_sftp",
                            "send_outgoing_webhook",
                            "send_to_integration",
                            "see_sql",
                            "see_lookml",
                            "develop",
                            "deploy",
                            "support_access_toggle",
                            "use_sql_runner",
                            "clear_cache_refresh",
                            "see_drill_overlay",
                            "manage_spaces",
                            "manage_homepage",
                            "manage_models",
                            "create_prefetches",
                            "login_special_email",
                            "embed_browse_spaces",
                            "embed_save_shared_space",
                            "see_alerts",
                            "see_queries",
                            "see_logs",
                            "see_users",
                            "sudo",
                            "see_schedules",
                            "see_pdts",
                            "see_datagroups",
                            "update_datagroups",
                            "see_system_activity",
                          "mobile_app_access"],
      models=["All"],
      group_ids=["5"],
      external_group_id="Sapphire_Test_Space",
      user_attributes={
                  "region": "New York", "country": "USA"})
  embed_sso=sdk.create_sso_embed_url(body = sso_body)
  return embed_sso.url


def get_lookml_dashboard_descriptions(files):
  reports = []
  pattern = '<[^<]+?>'
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

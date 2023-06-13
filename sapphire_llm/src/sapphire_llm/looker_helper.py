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


def generate_looker_url(dashboard_id: str, encoded_params = None) -> str:
  if encoded_params:
    target_url=f"https://cortexqa.cloud.looker.com/dashboards/{dashboard_id}?{encoded_params}"
  else:
    target_url=f"https://cortexqa.cloud.looker.com/dashboards/{dashboard_id}"
  sso_body = models40.EmbedSsoParams(
      target_url=target_url,
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
        subtitle_text = ''
        for i in range(len(fulfillment[0]['elements'])):
          element = fulfillment[0]['elements'][i]
          if 'title' in element:
            title = element['title'].rstrip()
            title_report = element['title'].replace(" ", "_")#.replace("%", "percent").replace("&", "and")
            # print(filename, title_report)

            if 'Untitled' not in title:
              # The filter attributes in the report.
              attributes = list(element['listen'].keys())
              if subtitle_text:
                # report = f'{title_report}: {subtitle_text} for {title} and the only information given is {attributes[0]} and {" and ".join(attributes[1:-1])}'
                report = f'{title_report}: {subtitle_text} for {title}'
              else:
                # report = f'{title_report}: {title} and the only information given is {attributes[0]} and {" and ".join(attributes[1:-1])}'
                if 'note_text' in element:
                  note_text = element['note_text'].rstrip()
                  report = f'{title_report}: {title} {note_text}'
                else:
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
  dashboard_id = ''
  for element in elements:
    dashboard_id = element.dashboard_id
    if element.result_maker:
      query_str = sdk.run_query(element.result_maker.query_id,result_format="sql")
      query_results = bq_helper.query(query_str)
      header = 'customers_name, sales'
      for i, row in enumerate(query_results):
        if row[1] is not None:
          results.append(f'{i+1}. {row[0]}, {human_format(row[1])}')
      break

  return (results, dashboard_id, header)


def get_query_results_with_filter(report_title_match, filtered_entities):
  print(report_title_match, filtered_entities)
  elements = sdk.search_dashboard_elements(title=report_title_match)
  dashboard_id = ''
  results = []
  mapped_columns = {}
  for element in elements:
    print("############# dashboard id: ", element.dashboard_id, " lookml: ", element.lookml_link_id, "entities: ", filtered_entities)
    dashboard_id = element.dashboard_id
    filter_fields = element.result_maker.filterables[0].listen

    filtered_entities['Timeframe Month'] = '3 months'
    filtered_entities['Timeframe Month'] = '3 months'
    filtered_entities['Date Month'] = '3 months'
    filtered_entities['Purchase Order Date'] = 'This Year'

    if 'Customer' in filtered_entities:
      filtered_entities['Supplier'] = "-" + filtered_entities['Customer'] # Use minus to indicate 'not'
    if 'Year' in filtered_entities:
      filtered_entities['Case Created Date'] = str(filtered_entities['Year'])

    for field_element in filter_fields:
      if field_element.dashboard_filter_name in filtered_entities.keys():
        if field_element.dashboard_filter_name == 'Year':
          mapped_columns[field_element.field] = str(filtered_entities[field_element.dashboard_filter_name])
        else:
          mapped_columns[field_element.field] = filtered_entities[field_element.dashboard_filter_name]

    altered_query = element.result_maker.query
    print("query_id:", altered_query.id, mapped_columns)
    altered_query.client_id = None
    altered_query.id = None
    altered_query.filters = mapped_columns # {field_element.field: value}
    query_str = sdk.run_inline_query(body=altered_query, result_format="sql")
    query_results = bq_helper.query(query_str)
    header = 'customers_name, sales'
    if 'time' in report_title_match.lower() or 'sales order' in report_title_match.lower():
      header = 'deliveries_date_created_erdat_month, deliveries_count_on_time_delivery, deliveries_count_in_full_delivery, deliveries_count_otif, deliveries_count_of_deliveries'
    elif 'news' in report_title_match.lower():
      header = 'month, company, number of articles'
    elif 'monthly' in report_title_match.lower():
      header = 'date, sales_volume_count, sales_volume_total_sales_price_net_document_currency'
    elif 'cases' in report_title_match.lower():
      header = 'open_cases, case_management_count'
    elif 'stock' in report_title_match.lower():
      header = 'product, vendor, product_stock_in_hand'
    elif 'delivery' in report_title_match.lower():
      header = 'date, vendor_performance_vendor_ontime, vendor_performance_infull_rate, vendor_performance_vendor_ontime_late'
    for i, row in enumerate(query_results):
      print(row)
      if row[0] is not None and row[1] is not None:
        if 'orders' in report_title_match.lower():
          results.append(f'{row[0]}, {row[1]}')
        elif 'monthly' in report_title_match.lower():
          results.append(f'{row[0]}, {row[1]}, {row[2]}')
        elif 'news' in report_title_match.lower():
          results.append(f'{row[0]}, {row[1]}, {row[2]}')
        elif 'time' in report_title_match.lower() or 'sales order' in report_title_match.lower():
          results.append(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')
        elif 'cases' in report_title_match.lower():
          results.append(f'{row[0]}, {row[1]}')
        elif 'stock' in report_title_match.lower():
          # results.append(f'{row[0]}, {row[2]}') # row[1] is defaul to None for some reason
          results.append((row[0],row[1], row[2]))
        elif 'delivery' in report_title_match.lower():
          results.append(f'{row[0]}, {round(row[1], 2)}, {round(row[2], 2)}, {round(row[3], 2)}') # row[1] is defaul to None for some reason
        else:
          results.append(f'{i+1}. {row[0]}, {human_format(row[1])}')
    break
  if results and 'stock' in report_title_match.lower():
    print("********** Sort stock *************")
    results = sorted(results, key=lambda x: x[2], reverse=True)
  return (results, dashboard_id, header)
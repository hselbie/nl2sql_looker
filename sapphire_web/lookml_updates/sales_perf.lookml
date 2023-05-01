- dashboard: sales_performance
  title: Sales Performance
  layout: newspaper
  preferred_viewer: dashboards-next
  description: Insights into sales performance with top-level and detailed KPIs relating
    to sales of top 10 products and customers.  Can filter sales figures by sales
    organisations, distribution channels and sales divisions
  preferred_slug: c9mzxFg53Nqu0abaNzoNb1
  elements:
  - name: Sales Performance
    type: text
    title_text: Sales Performance
    subtitle_text: "<font color=\"#c1c1c1\">How are my Sales performing ?\t</font>"
    body_text: ''
    row: 2
    col: 0
    width: 19
    height: 1
  - title: Sales Performance by Top 10 Products
    name: Sales Performance by Top 10 Products
    model: cortex-demo-genai
    explore: sales_orders
    type: looker_column
    fields: [materials_md.material_text_maktx, sales_orders.sales_order_netvalue_global_currency_product]
    sorts: [sales_orders.sales_order_netvalue_global_currency_product desc]
    limit: 500
    column_limit: 50
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: true
    legend_position: center
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    y_axes: [{label: Sales Order Net Value, orientation: left, series: [{axisId: sales_orders.sales_order_netvalue_global_currency,
            id: sales_orders.sales_order_netvalue_global_currency, name: Sales Order
              Netvalue Global Currency}], showLabels: true, showValues: true, unpinAxis: false,
        tickDensity: default, tickDensityCustom: 5, type: linear}]
    x_axis_label: Product
    limit_displayed_rows_values:
      show_hide: show
      first_last: first
      num_rows: '10'
    hide_legend: false
    series_colors:
      sales_orders.sales_order_netvalue_global_currency: "#FDEC85"
      sales_orders.sales_order_netvalue_global_currency_product: "#FDEC85"
    defaults_version: 1
    hidden_fields: []
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
      Customer: sales_orders.sold_to_party_name
    row: 11
    col: 0
    width: 11
    height: 7
  - title: Sales Performance by Top 5 Sales Org
    name: Sales Performance by Top 5 Sales Org
    model: cortex-demo-genai
    explore: sales_orders
    type: looker_column
    fields: [sales_organizations_md.sales_org_name_vtext, sales_orders.sales_order_netvalue_global_currency_sales_org]
    sorts: [sales_orders.sales_order_netvalue_global_currency_sales_org desc]
    limit: 500
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: true
    legend_position: center
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    y_axes: [{label: Sales Order Net Value, orientation: left, series: [{axisId: sales_orders.sales_order_netvalue_global_currency,
            id: sales_orders.sales_order_netvalue_global_currency, name: Sales Order
              Netvalue Global Currency}], showLabels: true, showValues: true, unpinAxis: false,
        tickDensity: default, tickDensityCustom: 5, type: linear}]
    x_axis_label: Sales Org
    limit_displayed_rows_values:
      show_hide: show
      first_last: first
      num_rows: 0
    series_colors:
      filtered_data_intelligence_otc_sum_sales_order_net_value_1: "#A5EF55"
      sales_orders.sales_order_netvalue_global_currency: "#A5EF55"
      sales_orders.sales_order_netvalue_global_currency_sales_org: "#A5EF55"
    defaults_version: 1
    hidden_fields: []
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
    row: 11
    col: 11
    width: 11
    height: 7
  - title: Sales Performance by Distribution Channel
    name: Sales Performance by Distribution Channel
    model: cortex-demo-genai
    explore: sales_orders
    type: looker_pie
    fields: [distribution_channels_md.distribution_channel_name_vtext, sales_orders.sales_order_netvalue_global_currency_dist_channel]
    sorts: [sales_orders.sales_order_netvalue_global_currency_dist_channel desc]
    limit: 500
    dynamic_fields: [{measure: sum_of_sales_order_netvalue_local_currency, based_on: sales_orders.sales_order_netvalue_local_currency,
        expression: '', label: Sum of Sales Order Netvalue Local Currency, type: sum,
        _kind_hint: measure, _type_hint: number}, {measure: sum_of_sales_order_netvalue_local_currency_2,
        based_on: sales_orders.sales_order_netvalue_local_currency, expression: '',
        label: Sum of Sales Order Netvalue Local Currency, type: sum, _kind_hint: measure,
        _type_hint: number}, {measure: sum_of_sales_order_net_price_local_currency,
        based_on: sales_orders.sales_order_net_price_local_currency, expression: '',
        label: Sum of Sales Order Net Price Local Currency, type: sum, _kind_hint: measure,
        _type_hint: number}, {measure: sum_of_sales_order_netvalue_local_currency_3,
        based_on: sales_orders.sales_order_netvalue_local_currency, expression: '',
        label: Sum of Sales Order Netvalue Local Currency, type: sum, _kind_hint: measure,
        _type_hint: number}, {measure: sum_of_sales_order_netvalue_local_currency_4,
        based_on: sales_orders.sales_order_netvalue_local_currency, expression: '',
        label: Sum of Sales Order Netvalue Local Currency, type: sum, _kind_hint: measure,
        _type_hint: number}]
    value_labels: legend
    label_type: labPer
    inner_radius: 40
    series_colors:
      Wholesale Sales: "#FCCF41"
      Digital Sales: "#7CC8FA"
      Retail Sales: "#f56776"
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: false
    legend_position: center
    label_value_format: ''
    series_types: {}
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    defaults_version: 1
    hidden_fields: []
    y_axes: []
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
    row: 18
    col: 4
    width: 7
    height: 5
  - title: Sales Performance by Division
    name: Sales Performance by Division
    model: cortex-demo-genai
    explore: sales_orders
    type: looker_pie
    fields: [sales_orders.sales_order_netvalue_global_currency_division, divisions_md.division_name_vtext]
    sorts: [sales_orders.sales_order_netvalue_global_currency_division desc]
    limit: 500
    value_labels: legend
    label_type: labPer
    inner_radius: 40
    start_angle: 18
    color_application:
      collection_id: 1297ec12-86a5-4ae0-9dfc-82de70b3806a
      palette_id: 93f8aeb4-3f4a-4cd7-8fee-88c3417516a1
      options:
        steps: 5
    series_colors:
      '04': "#C8A7F9"
      '03': "#F29ED2"
      '02': "#ACE9F5"
      'null': "#FDEC85"
      Electronics: "#ACE9F5"
      Perishables: "#C8A7F9"
      Packaged Goods: "#AEC8C1"
    series_types: {}
    defaults_version: 1
    hidden_fields: []
    y_axes: []
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
    row: 18
    col: 11
    width: 11
    height: 5
  - title: Total Customers
    name: Total Customers
    model: cortex-demo-genai
    explore: sales_orders
    type: single_value
    fields: [count_of_customer_number_kunnr_2]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: count_of_customer_number_kunnr, based_on: customers_md.customer_number_kunnr,
        expression: '', label: Count of Customer Number Kunnr, type: count_distinct,
        _kind_hint: measure, _type_hint: number, id: P6OqIto7kp}, {measure: count_of_customer_number_kunnr_2,
        based_on: customers_md.customer_number_kunnr, expression: '', label: Count
          of Customer Number Kunnr, type: count_distinct, _kind_hint: measure, _type_hint: number}]
    custom_color_enabled: true
    show_single_value_title: true
    show_comparison: false
    comparison_type: value
    comparison_reverse_colors: false
    show_comparison_label: true
    enable_conditional_formatting: false
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    show_view_names: false
    show_row_numbers: true
    truncate_column_names: false
    hide_totals: false
    hide_row_totals: false
    table_theme: editable
    limit_displayed_rows: false
    defaults_version: 1
    series_types: {}
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
    row: 18
    col: 0
    width: 4
    height: 5
  - title: Top Products for the Year
    name: Top Products for the Year
    model: cortex-demo-genai
    explore: sales_orders
    type: looker_column
    fields: [materials_md.material_text_maktx, sales_orders.sales_order_net_price_global_currency]
    sorts: [sales_orders.sales_order_net_price_global_currency desc 0]
    limit: 500
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: true
    legend_position: center
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    y_axes: [{label: Average Sales, orientation: left, series: [{axisId: sales_orders.sales_order_net_price_global_currency,
            id: sales_orders.sales_order_net_price_global_currency, name: Sales Order
              Net Price Global Currency}], showLabels: true, showValues: true, unpinAxis: false,
        tickDensity: default, tickDensityCustom: 5, type: linear}]
    x_axis_label: Product
    limit_displayed_rows_values:
      show_hide: show
      first_last: first
      num_rows: '10'
    series_types: {}
    series_colors:
      sales_orders.sales_order_net_price_global_currency: "#F29ED2"
    defaults_version: 1
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
      Customer: sales_orders.sold_to_party_name
    row: 3
    col: 11
    width: 11
    height: 8
  - title: New Tile
    name: New Tile
    model: cortex-demo-genai
    explore: sales_orders
    type: single_value
    fields: [sales_orders.dash_nav]
    limit: 500
    column_limit: 50
    custom_color_enabled: true
    show_single_value_title: true
    show_comparison: false
    comparison_type: value
    comparison_reverse_colors: false
    show_comparison_label: true
    enable_conditional_formatting: false
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    series_types: {}
    defaults_version: 1
    listen:
      Year: sales_orders.creation_date_erdat_date
      Division: divisions_md.division_name_vtext
      Currency: currency_conversion_new.tcurr
      Region: countries_md.country_name_landx
      Sales Org: sales_organizations_md.sales_org_name_vtext
      Distribution Channel: distribution_channels_md.distribution_channel_name_vtext
      Product: materials_md.material_text_maktx
      Customer: sales_orders.sold_to_party_name
    row: 0
    col: 0
    width: 22
    height: 2
  - title: Top Customers for the Year
    name: Top Customers for the Year
    model: cortex-demo-genai
    explore: sales_volume
    type: looker_column
    fields: [customers_md.name1_name1, sum_of_net_price_netpr, average_of_net_price_netpr]
    filters:
      sales_volume.creation_date_erdat_month: 2022/07/01 to 2023/04/30
    sorts: [sum_of_net_price_netpr desc 0]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: sum_of_net_price_netpr, based_on: sales_volume.net_price_netpr,
        expression: '', label: Sum of Net Price Netpr, type: sum, _kind_hint: measure,
        _type_hint: number}, {measure: average_of_net_price_netpr, based_on: sales_volume.net_price_netpr,
        expression: '', label: Average of Net Price Netpr, type: average, _kind_hint: measure,
        _type_hint: number}]
    query_timezone: Europe/Berlin
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: false
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: false
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: false
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: true
    legend_position: center
    point_style: circle
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    y_axes: [{label: Total Sales (USD), orientation: left, series: [{axisId: sum_of_net_price_netpr,
            id: sum_of_net_price_netpr, name: Sum of Net Price Netpr}], showLabels: true,
        showValues: true, valueFormat: "$#,##0", unpinAxis: false, tickDensity: default,
        type: linear}, {label: Avg. Sales (USD), orientation: right, series: [{axisId: average_of_net_price_netpr,
            id: average_of_net_price_netpr, name: Average of Net Price Netpr}], showLabels: true,
        showValues: true, valueFormat: "$#,##0.00", unpinAxis: false, tickDensity: default,
        type: linear}]
    x_axis_label: Customer
    x_axis_zoom: true
    y_axis_zoom: true
    limit_displayed_rows_values:
      show_hide: show
      first_last: first
      num_rows: '10'
    label_value_format: ''
    series_types:
      sum_of_net_price_netpr: area
    series_labels:
      sales_volume.average_sales_price_net_document_currency: Avg. Order Value (Document
        Currency)
      sum_of_net_price_netpr: Total Sales (local currency USD)
      average_of_net_price_netpr: Avg. Sales (local currency USD)
    defaults_version: 1
    hidden_fields: []
    hidden_points_if_no: []
    hidden_pivots: {}
    note_state: collapsed
    note_display: above
    note_text: Average and total sales of top customers for the year
    listen: {}
    row: 3
    col: 0
    width: 11
    height: 8
  filters:
  - name: Year
    title: Year
    type: field_filter
    default_value: 2022/10/01 to 2023/03/31
    allow_multiple_values: true
    required: false
    ui_config:
      type: day_range_picker
      display: inline
      options: []
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: sales_orders.creation_date_erdat_date
  - name: Currency
    title: Currency
    type: field_filter
    default_value: USD
    allow_multiple_values: true
    required: true
    ui_config:
      type: dropdown_menu
      display: inline
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: currency_conversion_new.tcurr
  - name: Region
    title: Region
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: countries_md.country_name_landx
  - name: Sales Org
    title: Sales Org
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: sales_organizations_md.sales_org_name_vtext
  - name: Distribution Channel
    title: Distribution Channel
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: distribution_channels_md.distribution_channel_name_vtext
  - name: Division
    title: Division
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: divisions_md.division_name_vtext
  - name: Product
    title: Product
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: materials_md.material_text_maktx
  - name: Customer
    title: Customer
    type: field_filter
    default_value: ''
    allow_multiple_values: true
    required: false
    ui_config:
      type: checkboxes
      display: popover
    model: cortex-demo-genai
    explore: sales_orders
    listens_to_filters: []
    field: sales_orders.sold_to_party_name

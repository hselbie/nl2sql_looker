- dashboard: monthly_sales_volume
  title: Monthly Sales Volume
  layout: newspaper
  preferred_viewer: dashboards-next
  description: Insights into monthly sales volume and order count that can be filtered
    by customer names and specific time periods.
  preferred_slug: dnB01aPfsIdlNRPUsgR6hs
  elements:
  - title: Monthly Sales Volume
    name: Monthly Sales Volume
    model: cortex-demo-genai
    explore: sales_volume
    type: looker_column
    fields: [sales_volume.creation_date_erdat_month, sales_volume.count, sales_volume.total_sales_price_net_document_currency]
    fill_fields: [sales_volume.creation_date_erdat_month]
    filters: {}
    sorts: [sales_volume.creation_date_erdat_month]
    limit: 500
    column_limit: 50
    query_timezone: Europe/Berlin
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
    y_axes: [{label: '', orientation: left, series: [{axisId: sales_volume.total_sales_price_net_document_currency,
            id: sales_volume.total_sales_price_net_document_currency, name: Total
              Sales (in Document Currency)}], showLabels: true, showValues: true,
        unpinAxis: false, tickDensity: default, tickDensityCustom: 5, type: linear},
      {label: !!null '', orientation: right, series: [{axisId: sales_volume.count,
            id: sales_volume.count, name: Order Count}], showLabels: true, showValues: true,
        unpinAxis: false, tickDensity: default, tickDensityCustom: 5, type: linear}]
    x_axis_zoom: true
    y_axis_zoom: true
    series_types: {}
    show_row_numbers: true
    truncate_column_names: false
    hide_totals: false
    hide_row_totals: false
    table_theme: editable
    enable_conditional_formatting: false
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    defaults_version: 1
    listen:
      Creation Date Month: sales_volume.creation_date_erdat_month
      Customer: customers_md.name1_name1
    row: 0
    col: 0
    width: 24
    height: 12
  filters:
  - name: Customer
    title: Customer
    type: field_filter
    default_value: Standard Retail
    allow_multiple_values: true
    required: false
    ui_config:
      type: advanced
      display: popover
    model: cortex-demo-genai
    explore: sales_volume
    listens_to_filters: []
    field: customers_md.name1_name1
  - name: Creation Date Month
    title: Creation Date Month
    type: field_filter
    default_value: 2023/01/01 to 2023/04/30
    allow_multiple_values: true
    required: false
    ui_config:
      type: advanced
      display: popover
    model: cortex-demo-genai
    explore: sales_volume
    listens_to_filters: []
    field: sales_volume.creation_date_erdat_month

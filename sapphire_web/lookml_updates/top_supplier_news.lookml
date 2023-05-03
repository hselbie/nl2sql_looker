- dashboard: gdelt_for_top_suppliers_for_our_top_products
  title: GDELT for Top Suppliers for our Top Products
  layout: newspaper
  preferred_viewer: dashboards-next
  description: KPIs on sentiments related to overall news with focus on employee and
    labour related topics that could impact our top vendors for our top products and
    vendor  performance from GDELT on top vendors
  preferred_slug: rFFIIZVBY7NAB5LjkDdQPH
  elements:
  - title: News about Suppliers
    name: News about Suppliers
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_column
    fields: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.company, gdelt_news_sentiment.count]
    pivots: [gdelt_news_sentiment.date_month]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters: {}
    sorts: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.count desc 0]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: list_of_themes, based_on: gdelt_news_sentiment.themes,
        expression: '', label: List of Themes, type: list, _kind_hint: measure, _type_hint: list},
      {measure: count_of_themes, based_on: gdelt_news_sentiment.themes, expression: '',
        label: Count of Themes, type: count_distinct, _kind_hint: measure, _type_hint: number}]
    query_timezone: Europe/Berlin
    x_axis_gridlines: false
    y_axis_gridlines: true
    show_view_names: true
    show_y_axis_labels: true
    show_y_axis_ticks: true
    y_axis_tick_density: default
    y_axis_tick_density_custom: 5
    show_x_axis_label: true
    show_x_axis_ticks: true
    y_axis_scale_mode: linear
    x_axis_reversed: true
    y_axis_reversed: false
    plot_size_by_field: false
    trellis: ''
    stacking: ''
    limit_displayed_rows: false
    legend_position: center
    point_style: none
    show_value_labels: true
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    color_application: undefined
    y_axes: [{label: '', orientation: left, series: [{axisId: gdelt_news_sentiment.count,
            id: gdelt_news_sentiment.count, name: Gdelt News Sentiment}], showLabels: true,
        showValues: true, unpinAxis: false, tickDensity: default, tickDensityCustom: 5,
        type: log}]
    x_axis_label: Supplier
    x_axis_zoom: true
    y_axis_zoom: true
    trellis_rows: 5
    series_types: {}
    series_labels: {}
    reference_lines: []
    trend_lines: []
    font_size_main: ''
    orientation: auto
    style_gdelt_news_sentiment.date_month: "#3A4245"
    show_title_gdelt_news_sentiment.date_month: true
    title_placement_gdelt_news_sentiment.date_month: above
    value_format_gdelt_news_sentiment.date_month: ''
    show_comparison_gdelt_news_sentiment.company: true
    comparison_style_gdelt_news_sentiment.company: value
    comparison_show_label_gdelt_news_sentiment.company: false
    style_gdelt_news_sentiment.count: "#3A4245"
    show_title_gdelt_news_sentiment.count: true
    title_placement_gdelt_news_sentiment.count: above
    value_format_gdelt_news_sentiment.count: ''
    show_comparison_gdelt_news_sentiment.count: false
    style_gdelt_news_sentiment.company: "#3A4245"
    show_title_gdelt_news_sentiment.company: true
    title_placement_gdelt_news_sentiment.company: above
    value_format_gdelt_news_sentiment.company: ''
    show_null_points: true
    interpolation: linear
    defaults_version: 1
    hidden_fields:
    custom_color_enabled: true
    show_single_value_title: true
    show_comparison: false
    comparison_type: value
    comparison_reverse_colors: false
    show_comparison_label: true
    enable_conditional_formatting: false
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    show_row_numbers: true
    transpose: false
    truncate_text: true
    hide_totals: false
    hide_row_totals: false
    size_to_fit: true
    table_theme: white
    header_text_alignment: left
    header_font_size: 12
    rows_font_size: 12
    hidden_pivots: {}
    hidden_points_if_no: []
    value_labels: legend
    label_type: labPer
    listen:
      Date Month: gdelt_news_sentiment.date_month
      Supplier: gdelt_news_sentiment.company
    row: 0
    col: 0
    width: 11
    height: 6
  - title: Suppliers News Sentiment Details
    name: Suppliers News Sentiment Details
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_grid
    fields: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.company, gdelt_news_sentiment.count,
      average_of_negative_score]
    pivots: [gdelt_news_sentiment.date_month]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters:
      gdelt_news_sentiment.themes: "%STRIKE%,%PROTEST%,%LABOR%,%LABOUR^ %,%UNION%"
    sorts: [gdelt_news_sentiment.date_month desc, gdelt_news_sentiment.count desc
        0]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: sum_of_negative_score, based_on: gdelt_news_sentiment.neg_score,
        expression: '', label: Sum of Negative Score, type: sum, _kind_hint: measure,
        _type_hint: number}, {measure: median_of_negative_score, based_on: gdelt_news_sentiment.neg_score,
        expression: '', label: Median of Negative Score, type: median, _kind_hint: measure,
        _type_hint: number}, {measure: list_of_themes_v2, based_on: gdelt_news_sentiment.v2_themes,
        expression: '', label: List of Themes (V2), type: list, _kind_hint: measure,
        _type_hint: list}, {measure: average_of_negative_score, based_on: gdelt_news_sentiment.neg_score,
        expression: '', label: Average of Negative Score, type: average, _kind_hint: measure,
        _type_hint: number}]
    query_timezone: Europe/Berlin
    show_view_names: false
    show_row_numbers: true
    transpose: false
    truncate_text: true
    hide_totals: false
    hide_row_totals: false
    size_to_fit: true
    table_theme: white
    limit_displayed_rows: false
    enable_conditional_formatting: false
    header_text_alignment: left
    header_font_size: 12
    rows_font_size: 12
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    color_application: undefined
    x_axis_gridlines: false
    y_axis_gridlines: true
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
    x_axis_zoom: true
    y_axis_zoom: true
    trellis: ''
    stacking: normal
    legend_position: center
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
    hidden_pivots: {}
    defaults_version: 1
    listen:
      Date Month: gdelt_news_sentiment.date_month
      Supplier: gdelt_news_sentiment.company
    row: 6
    col: 0
    width: 23
    height: 5
  - title: News on Suppliers' Labor Issues
    name: News on Suppliers' Labor Issues
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_column
    fields: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.company, gdelt_news_sentiment.count]
    pivots: [gdelt_news_sentiment.date_month]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters:
      gdelt_news_sentiment.v2_themes: "%STRIKE%,%PROTEST%,%LABOR%,%UNION%,%LABOUR%"
    sorts: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.company]
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
    stacking: normal
    limit_displayed_rows: false
    legend_position: center
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: true
    show_silhouette: false
    totals_color: "#808080"
    color_application:
      collection_id: 1297ec12-86a5-4ae0-9dfc-82de70b3806a
      palette_id: f29a5dfe-5665-4644-be18-468392d6af10
      options:
        steps: 5
    y_axes: [{label: Article Count, orientation: left, series: [{axisId: 2023-02 -
              gdelt_news_sentiment.count, id: 2023-02 - gdelt_news_sentiment.count,
            name: 2023-02}, {axisId: 2023-03 - gdelt_news_sentiment.count, id: 2023-03
              - gdelt_news_sentiment.count, name: 2023-03}, {axisId: 2023-04 - gdelt_news_sentiment.count,
            id: 2023-04 - gdelt_news_sentiment.count, name: 2023-04}], showLabels: true,
        showValues: true, unpinAxis: false, tickDensity: default, tickDensityCustom: 5,
        type: linear}]
    x_axis_label: Supplier
    x_axis_zoom: true
    y_axis_zoom: true
    series_types: {}
    series_colors: {}
    hidden_pivots: {}
    defaults_version: 1
    listen:
      Date Month: gdelt_news_sentiment.date_month
      Supplier: gdelt_news_sentiment.company
    row: 0
    col: 11
    width: 12
    height: 6
  filters:
  - name: Date Month
    title: Date Month
    type: field_filter
    default_value: 3 months
    allow_multiple_values: true
    required: false
    ui_config:
      type: advanced
      display: popover
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    listens_to_filters: []
    field: gdelt_news_sentiment.date_month
  - name: Supplier
    title: Supplier
    type: field_filter
    default_value: "-Standard Retail"
    allow_multiple_values: true
    required: false
    ui_config:
      type: advanced
      display: popover
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    listens_to_filters: []
    field: gdelt_news_sentiment.company

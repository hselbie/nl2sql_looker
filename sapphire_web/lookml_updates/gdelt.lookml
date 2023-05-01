- dashboard: gdelt_for_customers
  title: GDELT for Customers
  layout: newspaper
  preferred_viewer: dashboards-next
  description: KPIs on sentiments related to overall news with focus on environmental,
    social and governance from the global news, trends and events database (GDELT)
    about top customers
  preferred_slug: LmFFgbzquYLoYvIBGqiGUm
  elements:
  - title: Customer in News
    name: Customer in News
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_column
    fields: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.company, gdelt_news_sentiment.count]
    pivots: [gdelt_news_sentiment.date_month]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters: {}
    sorts: [gdelt_news_sentiment.date_month desc, gdelt_news_sentiment.count desc
        0]
    limit: 500
    column_limit: 50
    dynamic_fields: [{category: dimension, description: '', label: Sentiment, value_format: !!null '',
        value_format_name: !!null '', calculation_type: bin, dimension: sentiment,
        args: [gdelt_news_sentiment.sentiment, '100', "-55", '66', !!null '', classic],
        _kind_hint: dimension, _type_hint: string}]
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
    show_value_labels: true
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    ordering: none
    show_null_labels: false
    show_totals_labels: true
    show_silhouette: false
    totals_color: "#808080"
    y_axes: [{label: Articles, orientation: left, series: [{axisId: 2023-04 - gdelt_news_sentiment.count,
            id: 2023-04 - gdelt_news_sentiment.count, name: 2023-04}, {axisId: 2023-03
              - gdelt_news_sentiment.count, id: 2023-03 - gdelt_news_sentiment.count,
            name: 2023-03}, {axisId: 2023-02 - gdelt_news_sentiment.count, id: 2023-02
              - gdelt_news_sentiment.count, name: 2023-02}], showLabels: true, showValues: true,
        unpinAxis: false, tickDensity: default, tickDensityCustom: 5, type: linear}]
    x_axis_zoom: true
    y_axis_zoom: true
    hidden_pivots: {}
    defaults_version: 1
    listen:
      Timeframe Month: gdelt_news_sentiment.date_month
      Customer: gdelt_news_sentiment.company
    row: 0
    col: 0
    width: 8
    height: 7
  - title: Customer ESG Sentiment
    name: Customer ESG Sentiment
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_grid
    fields: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.esgtheme, average_of_postive_score,
      average_of_negative_score, average_of_sentiment]
    pivots: [gdelt_news_sentiment.date_month]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters:
      gdelt_news_sentiment.esgtheme: "-other"
    sorts: [gdelt_news_sentiment.date_month, gdelt_news_sentiment.esgtheme]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: median_of_postive_score, based_on: gdelt_news_sentiment.pos_score,
        expression: '', label: Median of Postive Score, type: median, _kind_hint: measure,
        _type_hint: number}, {measure: median_of_negative_score, based_on: gdelt_news_sentiment.neg_score,
        expression: '', label: Median of Negative Score, type: median, _kind_hint: measure,
        _type_hint: number}, {measure: average_of_postive_score, based_on: gdelt_news_sentiment.pos_score,
        expression: '', label: Average of Postive Score, type: average, _kind_hint: measure,
        _type_hint: number}, {measure: average_of_negative_score, based_on: gdelt_news_sentiment.neg_score,
        expression: '', label: Average of Negative Score, type: average, _kind_hint: measure,
        _type_hint: number}, {measure: average_of_polarity, based_on: gdelt_news_sentiment.polarity,
        expression: '', label: Average of Polarity, type: average, _kind_hint: measure,
        _type_hint: number}, {measure: average_of_sentiment, based_on: gdelt_news_sentiment.sentiment,
        expression: '', label: Average of Sentiment, type: average, _kind_hint: measure,
        _type_hint: number}]
    query_timezone: Europe/Berlin
    show_view_names: false
    show_row_numbers: false
    transpose: false
    truncate_text: true
    hide_totals: false
    hide_row_totals: false
    size_to_fit: true
    table_theme: white
    limit_displayed_rows: false
    enable_conditional_formatting: true
    header_text_alignment: left
    header_font_size: '12'
    rows_font_size: '12'
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    show_sql_query_menu_options: false
    show_totals: true
    show_row_totals: true
    truncate_header: false
    series_labels:
      gdelt_news_sentiment.date_month: Year-Month
      average_of_postive_score: Avg. +
      average_of_negative_score: Avg -
      average_of_polarity: Avg. Polarity
      average_of_sentiment: Avg. Sentiment
      gdelt_news_sentiment.esgtheme: ESG Theme
    series_cell_visualizations:
      average_of_postive_score:
        is_active: true
      average_of_negative_score:
        is_active: true
      average_of_polarity:
        is_active: true
      average_of_sentiment:
        is_active: true
    series_text_format:
      gdelt_news_sentiment.date_month:
        bg_color: "#E52592"
    conditional_formatting: [{type: along a scale..., value: !!null '', background_color: "#1A73E8",
        font_color: !!null '', color_application: {collection_id: 7c56cc21-66e4-41c9-81ce-a60e1c3967b2,
          palette_id: 4620e8de-df7a-40e0-89d6-7401f6e64d96, options: {steps: 5, constraints: {
              min: {type: minimum}, mid: {type: number, value: 0}, max: {type: maximum}},
            mirror: true, reverse: false, stepped: false}}, bold: false, italic: false,
        strikethrough: false, fields: [average_of_sentiment]}]
    series_value_format:
      average_of_postive_score:
        name: decimal_1
        decimals: '1'
        format_string: "#,##0.0"
        label: Decimals (1)
        label_prefix: Decimals
      average_of_negative_score:
        name: decimal_1
        decimals: '1'
        format_string: "#,##0.0"
        label: Decimals (1)
        label_prefix: Decimals
      average_of_polarity:
        name: decimal_1
        decimals: '1'
        format_string: "#,##0.0"
        label: Decimals (1)
        label_prefix: Decimals
      average_of_sentiment:
        name: decimal_2
        decimals: '2'
        format_string: "#,##0.00"
        label: Decimals (2)
        label_prefix: Decimals
    x_axis_gridlines: false
    y_axis_gridlines: true
    y_axes: [{label: '', orientation: left, series: [{axisId: 2023-02 - median_of_postive_score,
            id: 2023-02 - median_of_postive_score, name: 2023-02 - Median of Postive
              Score}, {axisId: 2023-02 - median_of_negative_score, id: 2023-02 - median_of_negative_score,
            name: 2023-02 - Median of Negative Score}, {axisId: 2023-03 - median_of_postive_score,
            id: 2023-03 - median_of_postive_score, name: 2023-03 - Median of Postive
              Score}, {axisId: 2023-03 - median_of_negative_score, id: 2023-03 - median_of_negative_score,
            name: 2023-03 - Median of Negative Score}, {axisId: 2023-04 - median_of_postive_score,
            id: 2023-04 - median_of_postive_score, name: 2023-04 - Median of Postive
              Score}, {axisId: 2023-04 - median_of_negative_score, id: 2023-04 - median_of_negative_score,
            name: 2023-04 - Median of Negative Score}], showLabels: true, showValues: true,
        unpinAxis: false, tickDensity: default, tickDensityCustom: 5, type: linear}]
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
    stacking: ''
    legend_position: center
    series_types: {}
    point_style: none
    show_value_labels: false
    label_density: 25
    x_axis_scale: auto
    y_axis_combined: true
    trend_lines: [{color: "#000000", label_position: right, order: 3, period: 7, regression_type: linear,
        series_index: 1, show_label: true}]
    ordering: none
    show_null_labels: false
    show_totals_labels: false
    show_silhouette: false
    totals_color: "#808080"
    show_dropoff: true
    hidden_pivots: {}
    defaults_version: 1
    show_null_points: true
    interpolation: linear
    value_labels: legend
    label_type: labPer
    hidden_fields: []
    hidden_points_if_no: []
    listen:
      Timeframe Month: gdelt_news_sentiment.date_month
      Customer: gdelt_news_sentiment.company
    row: 7
    col: 0
    width: 16
    height: 4
  - title: News on Customer Expansions / New Stores
    name: News on Customer Expansions / New Stores
    model: cortex-demo-genai
    explore: gdelt_news_sentiment
    type: looker_column
    fields: [gdelt_news_sentiment.date_month, count_of_article_link]
    fill_fields: [gdelt_news_sentiment.date_month]
    filters:
      gdelt_news_sentiment.themes: "%EXPAND%,%OPEN%,%NEW STORE%"
    sorts: [gdelt_news_sentiment.date_month desc]
    limit: 500
    column_limit: 50
    dynamic_fields: [{measure: count_of_article_link, based_on: gdelt_news_sentiment.link,
        expression: '', label: Count of Article Link, type: count_distinct, _kind_hint: measure,
        _type_hint: number}]
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
    show_null_points: true
    interpolation: linear
    defaults_version: 1
    hidden_pivots: {}
    series_types: {}
    listen:
      Timeframe Month: gdelt_news_sentiment.date_month
      Customer: gdelt_news_sentiment.company
    row: 0
    col: 8
    width: 8
    height: 7
  filters:
  - name: Timeframe Month
    title: Timeframe Month
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
    explore: gdelt_news_sentiment
    listens_to_filters: []
    field: gdelt_news_sentiment.company

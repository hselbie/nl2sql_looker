- dashboard: supplier_stock_in_hand
  title: Supplier Stock in Hand
  layout: newspaper
  preferred_viewer: dashboards-next
  description: Overview of suppliers' stock in hand for special consigned stock category
    filtered by stock type (Unrestricted use)
  preferred_slug: 9HAIh178njDPq0UyK8zf6T
  elements:
  - title: Stock per Supplier for top products
    name: Stock per Supplier for top products
    model: cortex-demo-genai
    explore: stock_in_hand
    type: looker_column
    fields: [materials_md.material_text_maktx, vendors_md.name1, stock_in_hand.total_qty]
    pivots: [materials_md.material_text_maktx]
    filters:
      materials_md.material_text_maktx: Big Paper Towels,Medium Paper Towels,Small
        Paper Towels
      stock_in_hand.stock_type: A-Unrestricted use
      stock_in_hand.special_stock_indicator_sobkz: K
    sorts: [materials_md.material_text_maktx, stock_in_hand.total_qty desc 0]
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
    x_axis_label: Supplier
    x_axis_zoom: true
    y_axis_zoom: true
    defaults_version: 1
    hidden_pivots: {}
    listen: {}
    row: 0
    col: 0
    width: 12
    height: 9

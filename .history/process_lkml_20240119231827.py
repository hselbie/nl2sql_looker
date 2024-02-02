import lkml

with open('lookml/order_items.lkml') as f:
    lkml_file = lkml.load(f)

print(lkml_file)
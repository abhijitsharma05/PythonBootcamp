product = ("Laptop", 50000, "Black",'Samsung', "Electronics")
print(product)

print("second element",[1])

print("last 2 elements",[2])

if "Electronics" in product:
    print(True)
else:
    print(False)

product_prices = (1000, 1500, 1200, 1100, 900)
product_prices_list =list(product_prices)
print(max(product_prices))
print(min(product_prices))

for item in product:
    print(item, end=" , ")

product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print(product)

product_new_item = ("In Stock",)
product = product + product_new_item
print(product)


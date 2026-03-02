from collections import OrderedDict
n = int(input())
items = OrderedDict()
for i in range(n):
    data = input().split()
    item_name = " ".join(data[:-1])   # join all words except the last one
    price = int(data[-1])             # last element is the price
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price
for item, total_price in items.items():
    print(item, total_price)


prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print("This is an example of sorting using sorted Ascending")
# d1 = sorted(prices.items(),key=lambda x : x[0])
# print(d1)
# print("This is an example of sorting using sorted Descending")
# d2 = sorted(prices.items(),key=lambda x : x[1])
# print(d2)
#
# print(min_price)
# print(max_price)
#
# print("This is an example of sorting using Zip")
# print(prices_sorted)

prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}


print("The min key is",min(prices, key=lambda k: prices[k])) # Returns 'FB'
print("The max key is",max(prices, key=lambda k: prices[k]))

min_value = prices[min(prices, key=lambda k: prices[k])]
print("The min value of min key is",min_value)
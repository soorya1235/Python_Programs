
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
zip1 = zip(prices.values(), prices.keys())
# # min_price is (10.75, 'FB')
print("This the Zip of the dictionary",list(zip1))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print("Below is the output of sorted value in dictoanry")
print(prices_sorted)
print("This is an example of sorting using sorted Ascending")

#Below is other method of sorting dictionary

d1 = sorted(prices.items(),key=lambda x : x[0])
print(d1)
print("This is an example of sorting using sorted Descending")
d2 = sorted(prices.items(),key=lambda x : x[1])
print(d2)
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

print("the min key is ...",sorted(prices,key=lambda k:prices[k]))
print("The min key is",min(prices, key=lambda k: prices[k])) # Returns 'FB'
print("The max key is",max(prices, key=lambda k: prices[k]))

# min_value = prices[min(prices, key=lambda k: prices[k])]
# print("The min value of min key is",min_value)
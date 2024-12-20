#1
a = {"a", "b", "c"}
b = {1, 2, 3}

zipped_list = zip(a, b)
print(list(zipped_list))

#2

c = [1, 2, 3, 4, 5]
d = [100, 200, 300, 400 ,500]

for x, y in zip(c, d[::-1]):
    print(x, y)

#3

stocks = ["A", "B", "C"]
prices = [1000, 2250, 3750]

dictionary = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(dictionary)
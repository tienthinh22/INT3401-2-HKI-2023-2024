fruits = ["apple", "orange", "pears", "bananas"]
fruitPrices = {"apples": 2.0, "oranges": 1.5, "pears": 1.75}

for i in fruits:
	print(i + " for sale")

for i, j in fruitPrices.items():
	if (j < 2.0):
		print("%s cost %f a pound" % (i, j))
	else:
		print(i + " are too expensive")

print()

print(list(map(lambda x: x * x, [1, 2, 3])))
print(list(filter(lambda x: x > 3, [1, 2, 3, 4, 55, 4, 3, 2, 1])))

print()

nums = [1, 2, 3, 4, 5, 6]
plusOneNums = [x + 1 for x in nums]
oddNums = [x for x in nums if x % 2 == 1]
print(oddNums)
oddNumsPlusOne = [x + 1 for x in nums if x % 2 == 1]
print(oddNumsPlusOne)
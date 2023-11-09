fruitPrices = {"apple": 2.0, "orange": 1.5, "pear": 1.75}

def buyFruit(fruit, num):
	if fruit not in fruitPrices:
		print("Nope")
	else:
		cost = fruitPrices[fruit] * num
		print("That'll be " + str(cost) + " please")

if __name__ == '__main__':
	buyFruit("apple", 2.4)
	buyFruit("coconuts", 2)
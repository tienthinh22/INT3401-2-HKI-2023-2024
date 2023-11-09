class FruitShop:
	total = 0 #total number of fruit shops

	def __init__(self, name, fruitPrices):
		"""
			name: name of the shop
			fruitPrices: Dictionary e.g. {"apples": 2.00, "oranges": 1.50, "pears": 1.75}
		"""
		self.fruitPrices = fruitPrices
		self.name = name
		print("Welcome to " + name + " fruit shop")
		FruitShop.total += 1

	def getCostPerUnit(self, fruit):
		"""
			fruit: Fruit name
			Returns cost of "fruit" if "fruit" is in inventory, else return -1
		"""
		if fruit not in self.fruitPrices:
			return -1
		return self.fruitPrices[fruit]
	
	def getPriceOfOrder(self, orderList):
		"""
			orderList: List of tuples (fruit, num)
				fruit: fruit name
				num: amount of fruit ordered
			Returns total cost of the order
		"""

		total = 0
		for fruit, num in orderList:
			costPerUnit = self.getCostPerPound(fruit)
			if (costPerUnit != -1):
				total += num * costPerUnit
		
		return total
	
	def getName(self):
		return self.name
	
	def getFruitPrices(self):
		return self.fruitPrices
	
	def getTotal(self):
		return FruitShop.total
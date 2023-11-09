import FruitShop

berkeleyShop = FruitShop.FruitShop("the Berkeley Bowl", {"apple": 1.0, "orange": 1.5, "pear": 1.75})

print(berkeleyShop.getCostPerUnit("apple"))
print(berkeleyShop.getTotal())

otherFruitShop = FruitShop.FruitShop("The Stanford Mall", {"kiwi": 6.0, "apple": 4.5, "peach": 8.75})
print(otherFruitShop.getCostPerUnit("apple"))

print(berkeleyShop.getFruitPrices())

print(berkeleyShop.getTotal())
print(otherFruitShop.getTotal())
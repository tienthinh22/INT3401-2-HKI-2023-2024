fruits = ["apple", "orange", "pear", "banana"]
print(fruits[0])

print()

otherFruits = ["kiwi", "strawberry"]
print(fruits + otherFruits)

print()

print(fruits[-2])
print(fruits.pop())
print(fruits)
fruits.append("grapefruit")
print(fruits)
fruits[-1] = "pineapple"
print(fruits)

print()

print(fruits[0:2]) #for i = start; i < end
print(fruits[:3]) #for i = 0; i < end
print(fruits[2:]) #for i = 2; i < len(fruits)
print(len(fruits))

print()

listOfLists = [['a', 'b', 'c'], [1, 2, 3], ["one", "two", "three"]]
print(listOfLists[1][2])
print(listOfLists[0].pop())
print(listOfLists)

print()

aList = ['a', 'b', 'c']
print(aList.reverse())
print(aList)
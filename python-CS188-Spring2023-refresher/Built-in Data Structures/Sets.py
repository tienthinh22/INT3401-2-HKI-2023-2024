shapes = ["circle", "square", "triangle", "circle"]
setOfShapes = set(shapes)
#setOfShapes = {"circle", "square", "triangle", "circle"}

setOfShapes.add("polygon")
print(setOfShapes)
print("circle" in setOfShapes)
print("rhombus" in setOfShapes)

print()

setOfFavoriteShapes = {"circle", "triangle", "hexagon"}
print(setOfShapes - setOfFavoriteShapes)
print(setOfShapes & setOfFavoriteShapes)
print(setOfShapes | setOfFavoriteShapes)
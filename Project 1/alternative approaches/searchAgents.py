def cornersHeuristic(state: Any, problem: CornersProblem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"
    
    import math

    def distance(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    length = len(state.getUnvisitedCorners())
    
    if (length == 0):
        return 0
    
    iteration = iter(state.getUnvisitedCorners())
    
    if (length == 1):
        heuristic = distance(state.getPosition(), next(iteration))

        return heuristic

    if (length == 2):
        corner0 = next(iteration)
        corner1 = next(iteration)

        heuristic = min(distance(state.getPosition(), corner0), distance(state.getPosition(), corner1)) + distance(corner0, corner1)

        return heuristic

    wallHeight = walls.height - 2
    wallWidth = walls.width - 2

    import sys
    minDist = sys.maxsize

    if (length == 4):
        for i in range(length):
            temp = distance(state.getPosition(), next(iteration))
            minDist = min(temp, minDist)

        heuristic = minDist + 2 * (min(wallHeight, wallWidth) - 1) + max(wallHeight, wallWidth) - 1

        return heuristic
    
    visitedCorner = (0, 0)

    for i in corners:
        if (not i in state.getUnvisitedCorners()):
            visitedCorner = i
            break
    
    oppositeVisitedCorner = (wallWidth - visitedCorner[0] + 1, wallHeight - visitedCorner[1] + 1)

    for i in state.getUnvisitedCorners():
        if (i != oppositeVisitedCorner):
            minDist = min(distance(state.getPosition(), i), minDist)

    heuristic = minDist + wallHeight + wallWidth - 2

    return heuristic #795

    return 0 # Default to trivial solution

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
		Inconsistent even after swaping mazeDistance with distance
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    foodList = foodGrid.asList()

    from util import manhattanDistance as distance

    if (len(foodList) == 0):
        return 0

    if ((len(foodList) == 1)):
        return distance(position, foodGrid[0])

    if ((len(foodList) == 2)):
        iteration = iter(foodList)
        return min(distance(position, next(iteration)), distance(position, next(iteration)))

    if (not problem.heuristicInfo):
        for i in foodList:
            for j in foodList:
                if (i != j and (j, i) not in problem.heuristicInfo):
                    problem.heuristicInfo[(i, j)] = mazeDistance(i, j, problem.startingGameState)

    maxDistance = 0
    maxFoods = ((0, 0), (0, 0))

    for foods, maxTemp in problem.heuristicInfo.items():
        if (maxTemp > maxDistance and foods[0] in foodList and foods[1] in foodList):
            maxDistance = maxTemp
            maxFoods = foods

    print(maxDistance, end = " ")
    print(maxFoods)

    return min(mazeDistance(position, maxFoods[0], problem.startingGameState), mazeDistance(position, maxFoods[1], problem.startingGameState)) + maxDistance

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    13898 #5
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = distance(closestFood, position)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    9551 #4
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    farthestFood = 0
    farthestFoodDistance = 0

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance > farthestFoodDistance):
            farthestFoodDistance = tempDistance
            farthestFood = i

    heuristic = distance(farthestFood, position)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Not admissible
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    farthestFood = 0
    farthestFoodDistance = 0

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance > farthestFoodDistance):
            farthestFoodDistance = tempDistance
            farthestFood = i

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = distance(farthestFood, position) + distance(closestFood, position)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Not admissible
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    farthestFood = 0
    farthestFoodDistance = 0

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance > farthestFoodDistance):
            farthestFoodDistance = tempDistance
            farthestFood = i

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = distance(farthestFood, position) + distance(closestFood, farthestFood)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Timeout
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = mazeDistance(position, i, problem.startingGameState)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = distance(closestFood, position)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Inconsistant
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    farthestFood = 0
    farthestFoodDistance = 0

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance > farthestFoodDistance):
            farthestFoodDistance = tempDistance
            farthestFood = i

    heuristic = mazeDistance(farthestFood, position, problem.startingGameState)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    7954 #3
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = mazeDistance(closestFood, position, problem.startingGameState)

    return heuristic

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    5543 #1
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = mazeDistance(closestFood, position, problem.startingGameState)

    for i in foodList:
        heuristic += 1

    return heuristic - 1 # The closest food

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Fail non-triviality
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = mazeDistance(closestFood, position, problem.startingGameState)

    for i in foodList:
        if (i[0] != position[0] and i[0] != closestFood[0]):
            heuristic += 1
        elif (i[1] != position[1] and i[1] != closestFood[1]):
            heuristic += 1

    return heuristic - 1

def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    5543 #2
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"

    from util import manhattanDistance as distance

    if (len(foodGrid.asList()) == 0):
        return 0

    foodList = foodGrid.asList()

    closestFood = 0
    closestFoodDistance = 999999

    for i in foodList:
        tempDistance = distance(position, i)

        if (tempDistance < closestFoodDistance):
            closestFoodDistance = tempDistance
            closestFood = i

    heuristic = mazeDistance(closestFood, position, problem.startingGameState)

    for i in foodList:
        if (i[0] != position[0] and i[0] != closestFood[0]):
            heuristic += 1
        elif (i[1] != position[1] and i[1] != closestFood[1]):
            heuristic += 1

    return heuristic

"""
	Note: the one with the higher heuristic is more likely to be better -> add all not-eaten foods
    Other approaches:
    First, ignore all the foods that is adjacent to 2 other foods. Keep all other foods
        (1) Find the shortest path through all foods by solving the Travelling Salesman Problem using Christofides algorithm and return the cost of the whole path as heuristic
        (2) Find all the choke points in the graph that when you remove a point, the graph splits into two smaller graphs. Find the shortest path through smaller graphs and add them later. (Just an idea, have no idea how to implement this)
"""
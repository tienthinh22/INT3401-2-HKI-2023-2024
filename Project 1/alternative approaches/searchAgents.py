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
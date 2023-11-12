class Node:
    def __init__(self, state, parent, action, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        
	#getters and setters

	#some function to return path from parents
        
def graphSearch(problem, dataStructure):
    visited = set()

    dataStructure.push((problem.getStartState(), list(), 0)) #(State, path to state, cost to state)
    
    while (not dataStructure.isEmpty()):
        temp = dataStructure.pop()

        if (temp[0] in visited):
            continue

        if (problem.isGoalState(temp[0])):
            return temp[1]

        visited.add(temp[0])

        # i[0] = position/state (x, y); i[1] = action to get there; i[2] = cost to get there from parent
        for i in problem.getSuccessors(temp[0]):
            if (i[0] not in visited):
                dataStructure.push((i[0], temp[1] + [i[1]], temp[2] + i[2]))

    print(problem.getStartState())

    return list()

#def graphSearch but for parent and action

'''
(Node class or tuples) and (path or parent + action)
=> 4 combinations
'''
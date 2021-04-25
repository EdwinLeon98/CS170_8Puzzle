from ProblemSpace import Problem
from Node import Node
import InputHandler, sys, heapq

# Initialize puzzle object
p = Problem()
p.setInit(InputHandler.getPuzzle())
algo = InputHandler.getAlgo()
print('Puzzle:')
p.printState(p.initState)

# Uniform Cost Search
count = 0
if algo == '1':
    initNode = Node()
    initNode.setG(0)
    initNode.setState(p.getInit())
    frontier = []
    heapq.heappush(frontier, initNode)
    explored = set()
    found = False
    while not found:
        if len(frontier) == 0:
            sys.exit('Error, frontier is empty')
        leaf = heapq.heappop(frontier)

        # If node contains a goal state return
        if p.isGoal(leaf.getState()):
            p.printState(leaf.getState())
            print(leaf.getG())
            sys.exit('Solution found')
        
        # Add node to explored
        explored.add(leaf)
        
        # Expand node adding results to frontier if new
        nodes = p.expand(leaf)
        count += 1
        for item in nodes:
            if not(item in frontier) and not(item in explored):
                heapq.heappush(frontier, item)
            else:
                pass

# A* Misplaced Tile Heuristic
elif algo == '2':
    pass

# A* Euclidean Distance Heuristic
elif algo == '3':
    pass
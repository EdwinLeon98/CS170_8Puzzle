from ProblemSpace import Problem
from Node import Node
import InputHandler, sys, heapq

# Initialize puzzle object
p = Problem()
p.setInit(InputHandler.getPuzzle())
algo = InputHandler.getAlgo()
p.printState(p.getInit())

# Uniform Cost Search
count = 0
maxQ = 1
if algo == '1':
    
    # Create node for initial state
    initNode = Node()
    initNode.setG(0)
    initNode.setState(p.getInit())
    
    # Put initial state node into frontier
    frontier = []
    heapq.heappush(frontier, initNode)
    
    # Initialize explored set to empty set
    explored = set()

    found = False
    while not found:
        if len(frontier) == 0:
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Frontier is empty')
        leaf = heapq.heappop(frontier)
        if maxQ < len(frontier):
            maxQ = len(frontier)

        # If node contains a goal state return
        if p.isGoal(leaf.getState()):
            solution = p.traceBack(leaf)
            solution.reverse()
            for i in range(1, len(solution)):
                print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(solution[i].getG(), solution[i].getH()))
                p.printState(solution[i].getState())
            print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(leaf.getG(), leaf.getH()))
            p.printState(leaf.getState())
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Solution found in ' + str(len(p.traceBack(leaf))) + ' moves')
        
        # Add node to explored
        explored.add(leaf)
        
        # Expand node adding results to frontier if new
        nodes = p.expandUCS(leaf)
        
        for item in nodes:
            if not(item in frontier) and not(item in explored):
                heapq.heappush(frontier, item)
                count += 1
            else:
                pass

# A* Misplaced Tile Heuristic
elif algo == '2':
    # Create node for initial state
    initNode = Node()
    initNode.setState(p.getInit())
    initNode.setG(0)
    initNode.setH(initNode.misplacedTiles())
    
    # Put initial state node into frontier
    frontier = []
    heapq.heappush(frontier, initNode)

    # Initialize explored set to empty set
    explored = set()

    found = False
    while not found:
        if len(frontier) == 0:
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Error, frontier is empty')
        leaf = heapq.heappop(frontier)
        if maxQ < len(frontier):
            maxQ = len(frontier)

        # If node contains a goal state return
        if p.isGoal(leaf.getState()):
            solution = p.traceBack(leaf)
            solution.reverse()
            for i in range(1, len(solution)):
                print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(solution[i].getG(), solution[i].getH()))
                p.printState(solution[i].getState())
            print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(leaf.getG(), leaf.getH()))
            p.printState(leaf.getState())
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Solution found in ' + str(len(p.traceBack(leaf))) + ' moves')
        
        # Add node to explored
        explored.add(leaf)
        
        # Expand node adding results to frontier if new
        nodes = p.expandA1(leaf)
        
        for item in nodes:
            if not(item in frontier) and not(item in explored):
                heapq.heappush(frontier, item)
                count += 1
            else:
                pass

# A* Euclidean Distance Heuristic
elif algo == '3':
    # Create node for initial state
    initNode = Node()
    initNode.setState(p.getInit())
    initNode.setG(0)
    initNode.setH(initNode.euclideanDist())
    
    # Put initial state node into frontier
    frontier = []
    heapq.heappush(frontier, initNode)

    # Initialize explored set to empty set
    explored = set()

    found = False
    while not found:
        if len(frontier) == 0:
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Error, frontier is empty')
        leaf = heapq.heappop(frontier)
        if maxQ < len(frontier):
            maxQ = len(frontier)

        # If node contains a goal state return
        if p.isGoal(leaf.getState()):
            solution = p.traceBack(leaf)
            solution.reverse()
            for i in range(1, len(solution)):
                print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(solution[i].getG(), solution[i].getH()))
                p.printState(solution[i].getState())
            print('The best state to expand with g(n) = {} and h(n) = {} is...\n'.format(leaf.getG(), leaf.getH()))
            p.printState(leaf.getState())
            print('Number of nodes expanded is ' + str(count))
            print('The maximum number of nodes in the queue at any one time: ' + str(maxQ))
            sys.exit('Solution found in ' + str(len(p.traceBack(leaf))) + ' moves')
        
        # Add node to explored
        explored.add(leaf)
        
        # Expand node adding results to frontier if new
        nodes = p.expandA2(leaf)
        for item in nodes:
            
            if not(item in frontier) and not(item in explored):
                heapq.heappush(frontier, item)
                count += 1
            else:
                pass
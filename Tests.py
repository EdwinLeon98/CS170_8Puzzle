from ProblemSpace import Problem
from Node import Node
import InputHandler, sys, heapq

# Initialize puzzle object
p = Problem()
p.setInit(InputHandler.getPuzzle())
print('Puzzle:')
p.printState(p.initState)
print()

n = Node()
n.setState(p.getInit())
n.setG(0)

n1 = Node()
n1.setState(p.getInit())
n1.setG(0)

explored = set()

frontier = []
if not n in frontier and not n in explored:
    heapq.heappush(frontier, n)
if not n in explored:
    explored.add(n)
if not n1 in frontier:
    heapq.heappush(frontier, n1)
if not n1 in explored:
    explored.add(n1)
print(len(frontier))
print(len(explored))

if not(p.transition(n, 'blank_left') == None):
    p.printState(p.transition(n, 'blank_left'))
else:
    print('transition is None')
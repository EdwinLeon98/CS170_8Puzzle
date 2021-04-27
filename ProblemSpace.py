from Node import Node

class Problem:
    def __init__(self):
        self.initState = []
        self.goalState = [['1','2','3'], ['4','5','6'], ['7','8','0']]
        self.actions = ['blank_up', 'blank_down', 'blank_left', 'blank_right']
        self.solution = []

    # Checks if the argument s is the goal state
    def isGoal(self, s):
        if s == self.goalState:
            return True
        else:
            return False

    # Sets the initial state to the argument s
    def setInit(self, s):
        for row in s:
            r = []
            for item in row:
                r.append(item)
            self.initState.append(r)

    def getInit(self):
        return self.initState

    # Print the puzzle information for a current state
    def printState(self, s):
        for i in range(len(s)):
            for j in range(len(s[0])):
                print(s[i][j], end=' ')
            print()

    def expandUCS(self, node):
        # return list of expanded nodes
        # expansion = []
        # check transition(node, a) for each action a, if transition returns valid state add it to expansion
        # return expansion
        expansion = []
        for a in self.actions:
            if not(self.transition(node, a) == None):
                n = Node()
                node.addChild(n)
                n.setG(node.getG() + 1)
                n.setState(self.transition(node, a))
                expansion.append(n)
        return expansion

    def expandA1(self, node):
        # return list of expanded nodes
        # expansion = []
        # check transition(node, a) for each action a, if transition returns valid state add it to expansion
        # return expansion
        expansion = []
        for a in self.actions:
            if not(self.transition(node, a) == None):
                n = Node()
                node.addChild(n)
                n.setH(node.misplacedTiles())
                n.setG(node.getG() + 1)
                n.setState(self.transition(node, a))
                expansion.append(n)
        return expansion

    def expandA2(self, node):
        # return list of expanded nodes
        # expansion = []
        # check transition(node, a) for each action a, if transition returns valid state add it to expansion
        # return expansion
        expansion = []
        for a in self.actions:
            if not(self.transition(node, a) == None):
                n = Node()
                node.addChild(n)
                n.setH(node.euclideanDist())
                n.setG(node.getG() + 1)
                n.setState(self.transition(node, a))
                expansion.append(n)
        return expansion

    def transition(self, node, action):
        # return result of state taking action, or 0 if returning bad state
        state = []
        for row in node.getState():
            new = []
            for item in row:
                new.append(item)
            state.append(new)
        
        blankPos = None
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == '0':
                    blankPos = i*3 + j
                    # Up
                    if action == self.actions[0]:
                        if blankPos > 2:
                            char = state[i-1][j]
                            state[i-1][j] = '0'
                            state[i][j] = char
                            return state
                        else:
                            return None

                    # Down
                    elif action == self.actions[1]:
                        if blankPos < 6:
                            char = state[i+1][j]
                            state[i+1][j] = '0'
                            state[i][j] = char
                            return state
                        else:
                            return None

                    # Left
                    elif action == self.actions[2]:
                        if not(blankPos%3 == 0):
                            char = state[i][j-1]
                            state[i][j-1] = '0'
                            state[i][j] = char
                            return state
                        else:
                            return None

                    #Right
                    elif action == self.actions[3]:
                        if not(blankPos==2) and not(blankPos==5) and not(blankPos==8):
                            char = state[i][j+1]
                            state[i][j+1] = '0'
                            state[i][j] = char
                            return state
                        else:
                            return None
                    else:
                        return None
        return state

    def traceBack(self, node):
        self.solution = []
        tmp = node
        while not(tmp.getParent() == None):
            self.solution.append(tmp.getParent())
            tmp = tmp.getParent()
        return self.solution
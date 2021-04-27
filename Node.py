import math

class Node():
    def __init__(self):
        self.state = []
        self.gofN = None
        self.hofN = 0
        self.parent = None
        self.children = []

    def addChild(self, c):
        if not(c in self.children):
            self.children.append(c)
            c.setParent(self)

    def __eq__(self, other):
        if other == None:
            return False
        return self.state == other.getState()

    def __hash__(self):
        return hash( (tuple(self.state[0]), tuple(self.state[1]), tuple(self.state[2])) )

    def __lt__(self, other):
        return self.gofN+self.hofN < other.gofN+other.hofN

    def setParent(self, p):
        if self.parent == None:
            self.parent = p

    def getParent(self):
        return self.parent

    def getG(self):
        return self.gofN

    def getH(self):
        return self.hofN

    def setG(self, g):
        self.gofN = g

    def setH(self, h):
        self.hofN = h

    def getState(self):
        return self.state

    def setState(self, s):
        self.state = s

    def misplacedTiles(self):
        goal = [['1','2','3'], ['4','5','6'], ['7','8','0']]
        count = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if not(self.state[i][j] == goal[i][j]) and not(self.state[i][j] == '0'):
                    count += 1
        return count

    def euclideanDist(self):
        goal = [['1','2','3'], ['4','5','6'], ['7','8','0']]
        dist = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if not(self.state[i][j] == goal[i][j]) and not(self.state[i][j] == '0'):
                    for n in range(len(goal)):
                        for m in range(len(goal[0])):
                            if self.state[i][j] == goal[n][m]:
                                dist += math.sqrt((n-i)**2 + (m-j)**2)
        return dist
class Node():
    def __init__(self):
        self.state = []
        self.gofN = None
        self.hofN = 0
        self.parent = None
        self.children = []

    # Add child c to self.children and update c's parent to this
    def addChild(self, c):
        if not(c in self.children):
            self.children.append(c)
            c.setParent(self)

    def __eq__(self, other):
        return self.state == other.getState()

    def __hash__(self):
        return hash( (tuple(self.state[0]), tuple(self.state[1]), tuple(self.state[2])) )

    def __lt__(self, other):
        return self.gofN+self.hofN < other.gofN+other.hofN

    # Sets this instance's parent to p
    def setParent(self, p):
        if self.parent == None:
            self.parent = p

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
class Problem:
    def __init__(self):
        self.initState = []
        self.goalState = [[1,2,3], [4,5,6],[7,8,0]]
        self.actions = []

    # Checks if the argument s is the goal state
    def isGoal(self, s):
        if s == self.goalState:
            return True
        else:
            return False

    # Sets the initial state to the argument s
    def setInit(self, s):
        for i in range(len(s)):
            new = []
            for j in range(len(s[0])):
                new.append(s[i][j])
            self.initState.append(new)

    # Print the puzzle information for a current state
    def printState(self, s):
        for i in range(len(s)):
            for j in range(len(s[0])):
                print(s[i][j], end=' ')
            print()
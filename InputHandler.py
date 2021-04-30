from ProblemSpace import Problem

# Puzzle Prompt
def getPuzzle():
    default = []
    
    print('Welcome to the 8 puzzle solver created by 862054277 and 862132870.')
    print('Authors: Josh McIntyre and Edwin Leon')
    invalidPuzzle = True
    while invalidPuzzle:
        puzzleChoice = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle: ')
        # Default puzzle input
        if puzzleChoice == '1':
            default = [['8','7','1'], ['6','0','2'], ['5','4','3']]
            invalidPuzzle = False

        # Custom puzzle input
        elif puzzleChoice == '2':
            print('Enter your puzzle, use a zero to represent the blank')
            # Row 1 prompt
            invalidRow = True
            while invalidRow:
                row1 = input('Enter the first row, use space or tabs between numbers: ').split()
                if not(len(set(row1)) == 3):
                    print('Error: Invalid numbers in row 1 please try again')
                    invalidRow = True
                else:
                    invalidRow = False
                    default.append(row1)
            
            #Row 2 prompt
            invalidRow = True
            while invalidRow:
                row2 = input('Enter the second row, use space or tabs between numbers: ').split()
                if not(len(set(row1+row2)) == 6):
                    print('Error: Invalid numbers in row 2 please try again')
                    invalidRow = True
                else:
                    invalidRow = False
                    default.append(row2)

            # Row 3 prompt
            invalidRow = True
            while invalidRow:
                row3 = input('Enter the third row, use space or tabs between numbers: ').split()
                if not(len(set(row1+row2+row3)) == 9):
                    print('Error: Invalid numbers in row 3 please try again')
                    invalidRow = True
                else:
                    invalidRow = False
                    default.append(row3)

            invalidPuzzle = False

            # Check if numbers in puzzle are in range [0,8]
            for i in range(len(default)):
                for j in range(len(default[0])):
                    if int(default[i][j]) < 0 or int(default[i][j]) > 8:
                        print('Error: Invalid number in puzzle, puzzle can only contain numbers in range [0,8]')
                        invalidPuzzle = True

            # If numbers in puzzle are out of range, empty the puzzle
            if invalidPuzzle:
                default = []

        # Invalid puzzle input, can only be 1 or 2
        else:
            print('Error: Invalid puzzle choice please try again')
            invalidPuzzle = True

    return default

# Algorithm Prompt
def getAlgo():
    algo = None
    invalidAlgo = True
    while invalidAlgo:
        algo = input('Enter 1 for Uniform Cost Search\nEnter 2 for A* with the Misplaced Tile heuristic\nEnter 3 for A* with the Eucledian distance heuristic\n')
        if algo == '1':
            print('You have selected Uniform Cost Search')
            invalidAlgo = False
        elif algo == '2':
            print('You have selected A* with the Misplaced Tile heuristic')
            invalidAlgo = False
        elif algo == '3':
            print('You have selected A* with the Eucledian distance heuristic')
            invalidAlgo = False
        else:
            print('Error: Invalid algorithm please try again')
            invalidAlgo = True
    return algo


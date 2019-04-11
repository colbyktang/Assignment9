# constants
FLOWER_MARKER = 'O'
INIT_MARKER = '#'
PLAYER_MARKER = 'K'

# board size
rowSize = 5
colSize = 5

# initialize boardMatrix
boardMatrix = [INIT_MARKER] * rowSize
for i in range(rowSize):
    boardMatrix[i] = [INIT_MARKER] * colSize

# initialize kangaroo
kangaroo_pos = [0,0]
kangaroo_dir = 0
boardMatrix[kangaroo_pos[0]][kangaroo_pos[1]] = PLAYER_MARKER;

# initialize game state booleans
isFlowerPicked = False
isFlowerPlanted = False

# initalize flower
flower_row = 0
flower_col = 3
boardMatrix[flower_row][flower_col] = FLOWER_MARKER

# print output
def printBoard ():
    global isFlowerPicked
    if (kangaroo_pos != [flower_row, flower_col] and not isFlowerPicked):
        boardMatrix[flower_row][flower_col] = FLOWER_MARKER
    for i in range(rowSize):
        string = ""
        for j in range(colSize):
            string += boardMatrix[i][j] + " "
        print (string)
    print ()


def hop(numOfHops):
    global kangaroo_dir
    global kangaroo_pos

    for i in range(numOfHops):
        boardMatrix[kangaroo_pos[0]][kangaroo_pos[1]] = INIT_MARKER;
        if (kangaroo_dir == 0):
            if (kangaroo_pos[0] - 1 >= 0):
                kangaroo_pos[0] -= 1
            else:
                print ("Kangaroo cannot move to the north!")
        elif (kangaroo_dir == 1):
            if (kangaroo_pos[1] + 1 < colSize):
                kangaroo_pos[1] += 1
            else:
                print ("Kangaroo cannot move to the east!")
        elif (kangaroo_dir == 2):
            if (kangaroo_pos[0] + 1< rowSize):
                kangaroo_pos[0] += 1
            else:
                print ("Kangaroo cannot move to the south!")
        elif (kangaroo_dir == 3):
            if (kangaroo_pos[1] - 1 >= 0):
                kangaroo_pos[1] -= 1
            else:
                print ("Kangaroo cannot move to the west!")
        boardMatrix[kangaroo_pos[0]][kangaroo_pos[1]] = PLAYER_MARKER;
        printBoard();
    
def pick():
    global isFlowerPicked
    global isFlowerPlanted
    
    if (not isFlowerPicked and kangaroo_pos == [flower_row, flower_col]):
        isFlowerPicked = True
        print ("Flower picked up!")
        
def plant():
    global isFlowerPicked
    global isFlowerPlanted
    global flower_row
    global flower_col
    
    if (isFlowerPicked):
        isFlowerPlanted = True
        isFlowerPicked = False
        print ("Flower planted!")
        flower_row = kangaroo_pos[0]
        flower_col = kangaroo_pos[1]
        boardMatrix[flower_row][flower_col] = FLOWER_MARKER
    
def turnRight():
    global kangaroo_dir
    kangaroo_dir = kangaroo_dir+1 % 4

def turnLeft():
    global kangaroo_dir
    kangaroo_dir = kangaroo_dir-1 % 4
        
def game():
    turnRight()
    hop(3)
    pick()
    turnRight()
    hop(2)
    plant()
    turnLeft()
    hop(1)

# start game
printBoard()
game()

import random

# constants
HIT_MARKER = 'X'
MISS_MARKER = 'O'
INIT_MARKER = '#'
PLAYER_MARKER = 'P'

# board size
rowSize = 5
colSize = 5

# enemy ship start
isEnemyAlive = True
enemy_row = random.randint(0,rowSize - 1)
enemy_col = random.randint(0,colSize - 1)

# player ship start
isPlayerAlive = True
playerShip_row = random.randint(0,rowSize - 1)
playerShip_col = random.randint(0,colSize - 1)
while (enemy_row == playerShip_row or enemy_col == playerShip_col):
    playerShip_row = random.randint(0,rowSize - 1)
    playerShip_col = random.randint(0,colSize - 1)

# save ship positions
enemyShipPositions = [[enemy_row, enemy_col]]
playerShipPositions = [[playerShip_row, playerShip_col]]
shipPositions = []
shipPositions.append (enemyShipPositions)
shipPositions.append(playerShipPositions)
print ("Player ship at", playerShipPositions)
print ("Enemy ship at", enemyShipPositions)
endMessage = "Game Over!"

# initialize boardMatrix
boardMatrix = [INIT_MARKER] * rowSize
for i in range(rowSize):
    boardMatrix[i] = [INIT_MARKER] * colSize

# set player marker
boardMatrix[playerShip_row][playerShip_col] = PLAYER_MARKER

# print output
def printBoard ():
    for i in range(rowSize):
        string = ""
        for j in range(colSize):
            string += boardMatrix[i][j] + " "
        print (string)

# calculate hit results
def calculateHit(row, col):
    global isPlayerAlive
    global isEnemyAlive
    global endMessage

    isHit = False
    for i in range(len(shipPositions)):
        if (shipPositions[i] == [[row,col]]):
            isHit = True
            if (row == playerShip_row and col == playerShip_col):
                print ("You got hit!")
                isPlayerAlive = False
                endMessage = "Game Over! You got hit!"
            elif (row == enemy_row and col == enemy_col):
                  isEnemyAlive = False
                  endMessage = "Game Over! You defeated the enemy ship!"
    if (isHit):
        boardMatrix[row][col] = HIT_MARKER
    else:
        boardMatrix[row][col] = MISS_MARKER

# game process
def game ():
    isGameRunning = True

    # keep the game running
    while (isGameRunning and isPlayerAlive and isEnemyAlive):
        isInputValid = False

        # input loop
        while (not isInputValid):
            player_input = input("Choose a row and a column, separated by a space: ").split()
            if (len(player_input) != 2):
                if (player_input[0] == "exit"):
                    print ("Exiting game...")
                    isGameRunning = False
                    return
                print ("Input invalid! Try again!")
            else:
                isInputValid = True

        # player input position
        player_row = int(player_input[0])
        player_col = int(player_input[1])

        # validate position
        if (player_row < 0 or player_row >= rowSize):
            print ("ROW OUT OF BOUNDS!")

        elif (player_col < 0 or player_col >= rowSize):
            print ("Column OUT OF BOUNDS!")

        # hit the board
        else:
            calculateHit (player_row, player_col)
            printBoard()
            
    # when game is over, print game over message
    print (endMessage)

# start game
printBoard()
game()

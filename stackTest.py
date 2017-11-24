letsLoop = True

myrow=[]
board = []
counter ="R"
opCounter ="B"
empty = ""
for xCoord in range(5):
    for yCord in range(8):
        myrow.append("{},{}".format(xCoord, yCord))
    board.append(myrow)
    myrow = []


while letsLoop == letsLoop:

    for myRowNumber in range(0,5):
        print(board[myRowNumber])
        
    column = int(input("Column number is: "))        

    for xCoord in range(5):
        print(board[xCoord][column])
        if board[xCoord][column] == counter or board[xCoord][column] == opCounter:
            board[xCoord - 1][column] = counter          
        elif xCoord == 4:
          board[4][column] = counter

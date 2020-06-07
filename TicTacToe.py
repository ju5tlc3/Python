from random import randrange

board = [[1,2,3],[4,5,6],[7,8,9]] #board[row][column]

def DisplayBoard():
    s = ('+'+'-'*7)*3+'+'
    y = ('|'+' '*7)*3+'|'
    print(s)
    for tup in board:
        print(y)
        print('|'+' '*2, tup[0],' '*2+
              '|'+' '*2, tup[1],' '*2+
              '|'+' '*2, tup[2],' '*2+'|')
        print(y + '\n' + s)

def EnterMove():
    var = int(input('Enter your move: '))
    if var in range(1,10):
        var-=1
        div = var//3
        rem = var % 3
        if board[div][rem] != 'X' and board[div][rem] != 'O':
            board[div][rem] = 'O'
            DisplayBoard()
            return
    print("Cell with",var+1, "number does not exist or busy\nPlease try one more time!")
    EnterMove()
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields():
    list_free = []
    for i in board:
        for j in i:
            if j != 'X' and j != 'O':
                list_free.append((i,j))
    return list_free
                
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def Winner(sign):
    print ("Game over.",end =' ')
    if sign == 'O':
       print("User won")
    else:
       print("Computer won")

def VictoryFor(sign):
    list_answers = []
    # 1) by row
    for i in board:
        for j in i:
            list_answers.append(sign == j)
        if False in list_answers:
            list_answers.clear()
        else:
            Winner(sign)
            return True
    # 2) by column
    for j in range(len(board)):
        for i in range(len(board)):
            list_answers.append(sign == board[i][j])
        if False in list_answers:
            list_answers.clear()
        else:
            Winner(sign)
            return True
    # 3) by diagonal
    for i in range(len(board)):
        list_answers.append(sign == board[i][i])
    if False in list_answers:
        list_answers.clear()
    else:
        Winner(sign)
        return True
    for i in range(len(board)):
        list_answers.append(sign == board[i][abs(2-i)])
    if False in list_answers:
        list_answers.clear()
    else:
        Winner(sign)
        return True
    if len(MakeListOfFreeFields()) == 0:
        print ("Game over. Draw")
        return True
    return False
    
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove():
    var = randrange(9)
    div  = var // 3
    rem = var % 3
    if board[div][rem] != 'X' and board[div][rem] != 'O':
        board[div][rem] = 'X'
        print("Computer takes the", var+1, "cell")
        DisplayBoard()
        return
    DrawMove()
# the function draws the computer's move and updates the board

DisplayBoard()
print("Let's decide who will be first")
if randrange(2) == 0:
    print("Computer's turn")
    DrawMove()
else:
    print("User's turn")
while len(MakeListOfFreeFields()) > 0:
    EnterMove()
    if VictoryFor('O'):
        break
    DrawMove()
    if VictoryFor('X'):
        break


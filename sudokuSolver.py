board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def findEmpty(board):
    for i in range(len(board)): # looping through rows of board
        for j in range(len(board[0])): #looping through column of board
            if board[i][j] == 0:
                return (i, j) #(row,col)

    return None #returning null if no empty position is found implying the board is fully solved

def valid(board, num, pos):

    #Checking if the number is already present in the same row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]: #looping through every row in the the same column and checking if number is found and also making sure that we do not check the same position that we just put a number in 
            return False

    #Checking if the number is present in the same column
    for i in range(len(board)):
        if board[i][pos[1]] ==  num and i != pos[0]:
            return False    

    #Checking if the number is already present in the box that we are putting the number in
    #Dividing the position,i.e either original row or column of the number's position, by 3 so that we can divide the whole board in 9 total boxes with indices (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)  
    box_x = pos[1] // 3  #finding the column of the box that we are putting the number in 
    box_y = pos[0] // 3  #finding the row of the box that we are putting the number in  

    for i in range(box_y*3, box_y*3 + 3):  #Multiplying the row index by 3 so that we get the original row index in our board and adding 3 so as there are 3 rows in each box 
        for j in range(box_x*3, box_x*3 + 3):  #Multiplying the column index by 3 so that we get the original column index in our board and adding 3 so as there are 3 columns in each box
            if board[i][j] == num and (i,j) != pos:
                return False      

    return True #if the number is found nowhere in row,column and box then returning true

def solve(board):
    find = findEmpty(board) #this returns the the position of empty 
    #if the findEmpty fuction gives nothing means there is no space empty the board is filled(solved) 
    if not find: 
        return True #so for False in find i.e solved board not find wiil be true,so we will return true
    else:
        row,col = find #if we get an empty position so find will be true and not find will be false and we will store the row & col of empty postion 
    
    for i in range(1,10):
        if valid(board, i, (row,col)): #so for empty space we will first put numbers from 1 to 10 and check if it is valid
            board[row][col] = i #if valid then we will put that number in empty postion 

            if solve(board): #then again we will do recurssion for next empty position by calling solve again
                return True
            
            #backtracking step,this is used when a number we put in the position is not valid, so we will make that postion zero and back track and reselect number for previous position we filled 
            board[row][col] = 0
    
    return False   #this false will be returned no number is valid for the empty position         

def printBoard(board):
    for i in range(len(board)): #looping through rows
        if i%3 == 0 and i != 0: #making a line after every 3 rows and excluding 0th row(i.e line before first row of numbers)
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])): #looping through columns
            if j % 3 == 0 and j != 0: #making a line after every 3 columns and excluding 0th column(i.e line before first column of numbers)
                print(" | ", end="") #end does not print \n i.e it does not go to a new line

            if j == 8:  # if at the last position then we print the number
                print(board[i][j])  
            else:
                print(str(board[i][j]) + " ", end="")   

printBoard(board)
solve(board)
print(" ")
print("Solution:")
printBoard(board)
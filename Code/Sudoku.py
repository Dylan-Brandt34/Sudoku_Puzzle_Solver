# 
#Sodoku consists of a 9 X 9 grid. Every row contains numbers 1 - 9 and every column has 1-9. No duplicates can exist in either row. 
# Example of a solved one can be found here https://sandiway.arizona.edu/sudoku/examples.html
# This program will use a backtracking algorithm to solve a sodoku puzzle and then dispay it out to the screen 

# How does it work:
#
# 1.) Recusively call a function that takes (row, column, and index of current check )
# 2.) Build a new list to build
#


startingPuzzle = [[ 5, 3, "", "", 7, "", "", "", "" ],
                  [ 6, "", "", 1, 9, 5, "", "", "" ],
                  [ "", 9, 8, "", "", "", "", 6, "" ], 
                  [ 8, "", "", "", 6, "", "", "", 3 ],
                  [ 4, "", "", 8, "", 3, "", "", 1 ],
                  [ 7, "", "", "", 2, "", "", "", 6 ],
                  [ "", 6, "", "", "", "", 2, 8, "" ],
                  [ "", "", "", 4, 1, 9, 6, 3, 5 ],
                  [ "", "", "", "", 8, "", "", 7, 9]
]
#startingPuzzle = [["",2,4,""],
#                  [1,"","",3],
#                  [4,"","",2],
#                  ["",1,3,""]
#                ]


#This class will represent each an entry in the sudoku puzzle (Maybe use a list?)
class Item: 
    Value = 0
    Editable = False
    def __init__(self, value):

        # if a value is equal to ("") then set the value to "blank"
        if value == "":
            self.Value = "blank"
        else: 
            self.Value = value

        # If a value exists when loading in the original then it is not editable
        if self.Value == "blank" :
            self.Editable = True
        else :
            self.Editable = False


# This is the class that will control the main functionality of the program
class SudokuSolver : 
    #Puzzle will hold the array of numbers 
    puzzle = []
    rowIterator = 0
    colIterator = 0
    #List that will tell an iteration when all numbers have been tried (maybe a little bit different than this actually)
    triedNums = []
    squares = []
    def __init__(self):
        puzzle = [] 
        triedNums = []
     
    #Constructor for the sodoku class
    def __init__(self, startingpuzzle):
        print("here is the starting puzzle")
        print(startingpuzzle)
        self.puzzle = []
        # Nested for loop to create the starting puzzle
        for row in startingpuzzle: 
            Line = []
            for item in row:
                # Here we will create each index as a list containing two datatype
                # 1.) the value of the position (either a number or null)
                # 2.) a boolean that states whether 
                x = Item(item)
                Line.append(x)
            self.puzzle.append(Line)
        print("The puzzle was loaded as follows:")
        for row in self.puzzle :
            for item in row:
                print( str(item.Value) + " " + str(item.Editable) )
        self.getSquares()
        print("here are the squares")
        for square in self.squares :
            print("start of square \n - \n - \n - \n")
            for item in square:
                print( str(item.Value) + " " + str(item.Editable) )
            print("\n\n\n end of square")
    

    #This method will take the puzzle and create the nine squares 
    def getSquares(self) :
        #Clear the squares and retrieve them all again 
        self.squares = []
        square1 = []
        square2 = []
        square3 = []
        rowIndex = 0
        for row in self.puzzle :
            colIndex = 0
            for item in row :
                if colIndex < 3: 
                    square1.append(item) 
                if colIndex >= 3 and colIndex < 6: 
                    square2.append(item) 
                if colIndex >=6 : 
                    square3.append(item)
                colIndex+=1
            rowIndex +=1
            if rowIndex > 2 :
                rowIndex = 0 
                self.squares.append(square1)
                self.squares.append(square2)
                self.squares.append(square3)
                square1 = []
                square2 = []
                square3 = []

    #This method will check the row and return if the item can be placed there 
    # Takes in the row iterator and a value. Returns whether the value exists in
    def CheckRow(self, value): 

        #iterate through the row to check if value is contained in any of the items 
        for item in self.puzzle[self.rowIterator] : 

            #If the value is found, return true
            if item.Value == value :
                return True     
        #if the end of the for loop is reached, then the value is not contained in the row.
        return False

    #This method will check the collumn and return if item can be place there 
    def CheckCol(self, value):
        for item in self.puzzle : 

            #If the value is found, return true
            if item[self.colIterator].Value == value :
                return True     
        #if the end of the for loop is reached, then the value is not contained in the row.
        return False

    
    #This method will check the "square" the item is in and return whether that number can be placed 
    def CheckBox(self, value): 
        tempSquare = []
        if self.rowIterator < 3 : 
            if self.colIterator < 3: 
                tempSquare = self.squares[0]
            if self.colIterator > 3 and self.colIterator < 6 :
                tempSquare = self.squares[1]
            if self.colIterator >= 6 : 
                tempSquare = self.squares[2]
        if self.rowIterator > 3 and self.rowIterator < 6 : 
            if self.colIterator < 3: 
                tempSquare = self.squares[3]
            if self.colIterator > 3 and self.colIterator < 6 :
                tempSquare = self.squares[4]
            if self.colIterator >= 6 : 
                tempSquare = self.squares[5]
        if self.rowIterator >= 6 : 
            if self.colIterator < 3: 
                tempSquare = self.squares[6]
            if self.colIterator > 3 and self.colIterator < 6 :
                tempSquare = self.squares[7]
            if self.colIterator >= 6 : 
                tempSquare = self.squares[8]
        for item in tempSquare : 
            if item.Value == value :
                return True     
        #if the end of the for loop is reached, then the value is not contained in the row.
        return False
       #This method will call all of the check methods and if all of them return false, then a value can be placed there 
    def check(self, value): 
        if self.checkRow(value) == False :
            if self.CheckCol(value) ==False :
                if self.CheckBox(value) == False :
                    return False
        else: 
            return True
            
    # Method to iterate the puzzle solver to the right. If the column iterator has reached the end, reset it and increase the row iterator
    def Iterate(self) : 
        if(self.colIterator == 8) : 
            self.colIterator = 0
            self.rowIterator +=1 
        else : 
            self.colIterator +=1
        return

    # method to backtrack in the case that no number can be put into a blank space
    # This method is called when the program realizes it has messed up 
    def Redo(self) : 
        if(self.colIterator == 0) :
            self.colIterator = 8 
            self.rowIterator -=1
        else : 
            self.colIterator -=1
        return 
            #This method will control the flow of solving the puzzle. It will decide whether to place a number or not
    def Main(self, sent):

        if self.puzzle[self.rowIterator][self.colIterator].Editable  == False :
            self.Iterate()
            #LOOK INTO HOW TO GET AROUND BACK TRACKING TO A VALUE AND SUBMITTING THE SAME THING 
            # EXAMPLE: 
            # 3, 4 ,X 
            # X doesn't work and the item before it [4] iterates from 1-4 and then selects 4 again
            # this could cause an endless recursion cycle!!!!!!!!!!!!!!!!!!!!!!!
        else:
            # Begin finding a number to place in the spot 
            for value in range(1, 10) : 
                if self.check(value) == False : 
                    #if false, then the value is not contained anywhere and can be placed. 



            #if no number works, back track until the first editable field is found 
        
        #proceed through main 
        return 0
 #- end of sodoku class----------------------------------------------------------------------------------------------------------------------------------------------------------       

#puzzle = SudokuSolver(startingPuzzle); 




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

        # if a value is equal to ("") then set the value to "blank" and editable to True
        if value == "":
            self.Value = "blank"
            self.Editable = True
          # if a value is NOT equal to ("") then set the value to the sent value and editable to False
        else: 
            self.Value = value
            self.Editable = False




# This is the class that will control the main functionality of the program
class SudokuSolver : 
#These are the created fields for the Sudoku solver object ------------------------------------------------------------------------------

    #isBacktracking is a boolean to decide whether the program is currently backtracking or not 
    isBacktracking = False 
    isSolved = False
    #Puzzle will hold the array of numbers 
    puzzle = []

    # Row iterator keeps up with current row the puzzle solver is on
    rowIterator = 0

    # Col iterator keeps up with current Column the puzzle solver is on
    colIterator = 0

    #Holds a list of all of the 3x3 squares in the puzzle
    squares = []

     
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
        self.printCurrentPuzzle()
        self.getSquares()
        print("here are the squares")
        for square in self.squares :
            print("start of square \n - \n - \n - \n")
            for item in square:
                print( str(item.Value) + " " + str(item.Editable) )
            print("\n\n\n end of square")
    

    def printCurrentPuzzle(self) : 
        print("\n\n\n\n\n\n")
        for row in self.puzzle :
            tempRow = []
            
            for item in row:
                tempRow.append(item.Value)
            print(tempRow)
        print("\n\n\n\n\n\n")
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
        if self.CheckRow(value) == False :
            if self.CheckCol(value) ==False :
                if self.CheckBox(value) == False :
                    return False
        else: 
            return True
            
    # Method to iterate the puzzle solver to the right. If the column iterator has reached the end, reset it and increase the row iterator
    def Iterate(self) : 
        self.isBacktracking = False
        if(self.colIterator == 8) : 
            self.colIterator = 0
            self.rowIterator +=1 
        else : 
            self.colIterator +=1
        return

    # method to backtrack in the case that no number can be put into a blank space
    # This method is called when the program realizes it has messed up 
    def Redo(self) : 
        self.isBacktracking = True
        if(self.colIterator == 0) :
            self.colIterator = 8 
            self.rowIterator -=1
        else : 
            self.colIterator -=1
        return 

#Old main that relied on recursion with the main method.
    #This method will control the flow of solving the puzzle. It will decide whether to place a number or not
#    def Main(self):
#        #Set the current item here
#       sent = self.puzzle[self.rowIterator][self.colIterator]
#
#        # if the item is not editable, iterate and then 
#        if sent.Editable  == False :
#            if self.isBacktracking == True : 
#                self.Redo()
#            else : 
#                self.Iterate()
#
#        else:
#          if sent.Value == "blank" : 
#                sent.Value = 1
#            # Begin finding a number to place in the spot 
#            for value in range(sent.Value, 10) : 
#                #if false, then the value is not contained anywhere and can be placed. 
#                if self.check(value) == False : 
#                    sent.Value = value
#                    self.getSquares() 
#                    break
#            # if the value at this position is still blank, then the puzzle should backtrack and change a previous value      
#            if sent.Value == "blank" : 
#                self.Redo()
#            #If it is not blank then iterate and call main again to repeat the process
#            else: 
#                self.Iterate
        

         
        #If the puzzle is not finished, then continue the recursion process
#        if sent.Value != "blank" and self.rowIterator != 8 and self.colIterator != 8 :
        #proceed through main 
#            self.Main()
#        return 0

         #This method will control the flow of solving the puzzle. It will decide whether to place a number or not
    def Main(self):
    
      #loop to iterate through the puzzle solving process
        while self.isSolved != True : 
              #Set the current item here
            sent = self.puzzle[self.rowIterator][self.colIterator]
            tempNumber = sent.Value
            # if the item is not editable, iterate and then 
            if sent.Editable  == False :
                if self.isBacktracking == True : 
                    self.Redo()
                else : 
                    self.Iterate()
            # The item is an editable field and will be filled with a number
            else:
                #if the field is blank, set the temp number to 1 
                if sent.Value == "blank" : 
                    tempNumber = 1
                # Begin finding a number to place in the spot 

                for value in range(tempNumber, 10) : 
                    #if false, then the value is not contained anywhere and can be placed. 
                    if self.check(value) == False : 
                        self.puzzle[self.rowIterator][self.colIterator].Value = value
                        self.getSquares() 
                        #self.printCurrentPuzzle()
                        break
                    tempNumber +=1
                # if the value at this position is still blank, then the puzzle should backtrack and change a previous value      
                if tempNumber == 10 : 
                    sent.Value = "blank"
                    self.Redo()
                #If it is not blank then iterate and call main again to repeat the process
                else: 
                    self.Iterate()
            

            #self.printCurrentPuzzle()
            #If the puzzle is not finished, then continue the recursion process
            if sent.Value != "blank" and self.rowIterator == 8 and self.colIterator == 8 :
            #proceed through main 
                self.isSolved = True
                self.printCurrentPuzzle()




 #- end of sodoku class----------------------------------------------------------------------------------------------------------------------------------------------------------       

puzzle = SudokuSolver(startingPuzzle) 
puzzle.Main() 


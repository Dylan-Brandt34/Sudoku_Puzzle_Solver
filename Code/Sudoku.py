
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
    rowiterator = 0
    coliterator = 0
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

            
      
    #This method will control the flow of solving the puzzle. It will decide whether to place a number or not
    def Main(self, sent):


        #Set up the main for the first time run through 
        #iterate through the code from row 1 and work through the rows from left to right 

        #iterate through the number 1-9 and (or x - 9 [x is the number the square was on initially]) place the first number that works into 

            #if no number works, back track until the first editable field is found 
        
        #proceed through main 
        return 0

    #This method will check the row and return if the item can be placed there 
    def CheckRow(self): 
        return False

    #This method will check the collumn and return if item can be place there 
    def CheckCol(self):
        return False

    #This method will check the "square" the item is in and return whether that number can be placed 
    def CheckBox(): 
        return False
 #- end of sodoku class----------------------------------------------------------------------------------------------------------------------------------------------------------       

puzzle = SudokuSolver(startingPuzzle); 




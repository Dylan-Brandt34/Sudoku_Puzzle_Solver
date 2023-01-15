import unittest
from Sudoku import SudokuSolver
from Item import Item

#Global variable that holds the Sudoku puzzle 
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
class PuzzleTest(unittest.TestCase) :

    #test that the value is being set
    #  [ the sudoku puzzle will be composed of a 2d array of "item" objects]
    def setUp(self) : 
         solver = SudokuSolver(startingPuzzle)
    def testItemSet(self) : 
        item = Item(2)
        self.assertEqual(item.Value , 2, "Incorrect")
    #test that the editable field is being set correctly
    def testItemEdit(self) :
        item = Item(2)
        #test that an item sent a value is not editable
        self.assertEqual(item.Editable, False, "Incorrect")

        #test that an item not sent a value is editable
        item = Item("")
        self.assertEqual(item.Editable, True, "Incorrect")

    #Tests the Constructer functions with SudokuSolver class
    def testSudokuSolverConstructer(self) :
        solver = SudokuSolver(startingPuzzle)
        #confirm that there are 9 rows
        self.assertEqual(len(solver.puzzle), 9, "Incorrect")

        #confirm that there at 9 columns in a row
        self.assertEqual(len(solver.puzzle[0]), 9, "Incorrect")

        self.assertEqual(len(solver.squares[0]), 9, "Incorrect")
        items = []
        for item in solver.squares[0] :
            items.append(item)
            
        print("These are the square contents")
        for item in items : 
            print(item.Value)

        #Assert that the first and last item in the square is correct. Maybe have a better verifaction method? 
        self.assertEqual(solver.squares[0][0].Value, 5 , "incorrect")
        self.assertEqual(solver.squares[0][8].Value, 8 , "incorrect")

    #Tests that the row check method will return true when a value is contained and false when a value is not contained
    def testSudoku_Row_Method(self) : 
        solver = SudokuSolver(startingPuzzle)

        # the value 5 should exist in the first row
        self.assertEqual(solver.CheckRow(5), True)

        #the value 9 should not exist in the row 
        self.assertEqual(solver.CheckRow(9), False)

    #Tests that the Column Check method will return true when a value is contained and false when a value is not contained
    def testSudoku_Col_Method(self) : 
        solver = SudokuSolver(startingPuzzle)
        solver.colIterator = 0
        # the value 5 should exist in the first row
        self.assertEqual(solver.CheckCol(5), True)

        #the value 9 should not exist in the row 
        self.assertEqual(solver.CheckCol(9), False)
    #Tests that each square holds the correct value 
    def testSudoku_Square_Method(self) : 
        solver = SudokuSolver(startingPuzzle)

# Come back and figure out the best way to test this.
        #the value 5 should exist in the top left square 
        self.assertEqual(solver.CheckSquare(5), True)

        #the value 7 should NOT exist in the top left square 
        self.assertEqual(solver.CheckSquare(7), False)

    def testUpdateSquare (self) : 
        solver = SudokuSolver(startingPuzzle)
        solver.colIterator = 2 
        solver.rowIterator = 2
        solver.updateSquare(3)

        
        
    # Tests the iterate function.
    # Makes sure when the colIterator reaches 9, the col Iterator is set to 0 and the row iterator is increased 
    def testPuzzleIterator (self) : 
        solver = SudokuSolver(startingPuzzle)
        solver.colIterator = 0
        solver.Iterate()
        self.assertEqual(solver.colIterator, 1 )
        solver.rowIterator =0 
        solver.colIterator = 8
        solver.Iterate() 
        self.assertEqual(solver.colIterator, 0)
        self.assertEqual(solver.rowIterator, 1)

    #Tests the Redo method much like how the iterate method was tested  
    def testPuzzleRedo(self) : 
        solver = SudokuSolver(startingPuzzle)
        solver.colIterator = 1
        solver.rowIterator = 0
        solver.Redo()
        self.assertEqual(solver.colIterator, 0 )
        self.assertEqual(solver.rowIterator, 0)
        solver.rowIterator =1
        solver.colIterator = 0
        solver.Redo() 
        self.assertEqual(solver.colIterator, 8)
        self.assertEqual(solver.rowIterator, 0)
       
    
    def testMain(self) : 
           solver = SudokuSolver(startingPuzzle)
           solver.Main()
    # Maybe test main? 


if __name__ == '__main__':
    unittest.main()
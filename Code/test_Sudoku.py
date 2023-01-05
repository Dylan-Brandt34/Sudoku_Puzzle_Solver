import unittest
from Sudoku import Item , SudokuSolver

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
    def testItemSet(self) : 
        item = Item(2)
        self.assertEqual(item.Value , 2, "Incorrect")
##test that the editable field is being set correctly
    def testItemEdit(self) :
        item = Item(2)
        #test that an item sent a value is not editable
        self.assertEqual(item.Editable, False, "Incorrect")

        #test that an item not sent a value is editable
        item = Item("")
        self.assertEqual(item.Editable, True, "Incorrect")

    def testSudokuSolver(self) :
        solver = SudokuSolver(startingPuzzle)
        #confirm that there are 9 rows
        self.assertEqual(len(solver.puzzle), 9, "Incorrect")

        #confirm that there at 9 columns in a row
        self.assertEqual(len(solver.puzzle[0]), 9, "Incorrect")

 

if __name__ == '__main__':
    unittest.main()
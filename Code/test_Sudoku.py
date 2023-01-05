import unittest
from Sudoku import Item , SudokuSolver


class PuzzleTest(unittest.TestCase) :

    def testItemSet(self) : 
        item = Item(2)
        
        #test that the value is being set
        self.assertEqual(item.Value , 2, "Incorrect")

    def testItemEdit(self) :
        item = Item(2)
        #test that an item sent a value is not editable
        self.assertEqual(item.Editable, False, "Incorrect")

        item = Item("")
        self.assertEqual(item.Editable, True, "Incorrect")
#
#   def testSudokuSolver(self) :
#        solver = SudokuSolver([
#                  ["",2,4,""],
#                  [1,"","",3],
#                  [4,"","",2],
#                  ["",1,3,""]
#                ])
#        print(solver.puzzle.count)
#        self.assertEqual(solver.puzzle.count, 4, "Incorrect")


unittest.main()
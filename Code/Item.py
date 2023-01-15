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

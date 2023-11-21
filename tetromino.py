import numpy as np

class Tetromino: 

    def __init__(self, letter, orientation = 0):
        ''''''
        self._shape_dict = {0:[[1,1,1,1]],
                            1:[[1,0,0],[1,1,1]],
                            2:[[0,0,1],[1,1,1]],
                            3:[[1,1],[1,1]],
                            4:[[0,1,1],[1,1,0]],
                            5:[[0,1,0],[1,1,1]],
                            6:[[1,1,0],[0,1,1]],
                            }
        self.letter = letter
        self.shape = self.get_shape(letter)
        self.orientation = orientation
        

    def get_shape(self):
        return self.shape_dict[self.letter]
        

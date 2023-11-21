import numpy as np

class Tetromino: 

    def __init__(self, letter, orientation = 0):
        ''''''
        self._shape_dict = {1:[[1,1,1,1]],
                            2:[[2,0,0],[2,2,2]],
                            3:[[0,0,3],[3,3,3]],
                            4:[[4,4],[4,4]],
                            5:[[0,5,5],[5,5,0]],
                            6:[[0,6,0],[6,6,6]],
                            7:[[6,6,0],[0,6,6]],
                            }
        self.letter = letter
        self.orientation = orientation
        self.get_shape()
        

    def get_shape(self):
        self.block = self._shape_dict[self.letter]
        print(self.block)
        self.block = np.rot90(self.block, k=self.orientation)
        print(self.block)


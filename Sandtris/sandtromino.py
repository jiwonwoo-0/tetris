import numpy as np


class Sandtromino:
    """
    Sandtromino piece

    Attributes:
        _shape_dict (dict): map of tetromino type to shapes
        letter (int): letter (coded to a number) representing tetromino type
        orientation (int): current orientation of tetromino (0, 1, 2, or 3)
        block (numpy.ndarray): current tetromino shape
        r (int): Row index of tetromino in the playfield
        c (int): Column index of tetromino in the playfield
    """

    def __init__(self, letter, orientation=0, scale=3):
        """
        Initializes a Tetromino with a specified letter and orientation

        Parameters:
            letter (int): letter (coded to a number) representing tetromino type
            orientation (int): current orientation of tetromino (0, 1, 2, or 3)
            scale (int): scaling factor for the tetromino
        """
        self.letter = letter
        self.scale = scale
        self._shape_dict = {
            1: [[1, 1, 1, 1]],
            2: [[2, 0, 0], [2, 2, 2]],
            3: [[0, 0, 3], [3, 3, 3]],
            4: [[4, 4], [4, 4]],
            5: [[0, 5, 5], [5, 5, 0]],
            6: [[0, 6, 0], [6, 6, 6]],
            7: [[7, 7, 0], [0, 7, 7]],
        }
        self.orientation = orientation
        self.get_shape()
        self.r = 0
        self.c = 0

    def get_shape(self):
        """
        Sets current shape of tetromino based on its letter and orientation
        """
        self.block = self._shape_dict[self.letter]
        self.block = np.rot90(self.block, k=self.orientation)
        self.block = np.repeat(self.block, self.scale, axis=0)
        self.block = np.repeat(self.block, self.scale, axis=1)

    def rotate(self, k=1):
        """
        Rotates the tetromino 90-degrees clockwise k times

        Parameters:
            k (int): Number of rotations
        """
        self.orientation += k
        self.block = np.rot90(self.block, k=k)

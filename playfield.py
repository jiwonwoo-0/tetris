import numpy as np

class Playfield:

    def __init__(self):
        self.pf = np.zeros((20, 10))
    
    def add_t(self, t):
        for i in range(t.block.shape[0]):
            for j in range(t.block.shape[1]):
                if t.block[i,j] != 0:
                    self.pf[i+t.r, j+t.c] = t.block[i,j]
    
    def clear_line(self, row):
        self.pf = np.delete(self.pf, row, 0)
        self.pf = np.insert(self.pf, 0, np.zeros(10), 0)
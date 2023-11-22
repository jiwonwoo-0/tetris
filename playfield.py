import numpy as np

class Playfield:

    def __init__(self):
        self.pf = np.zeros((20, 10))
    
    def update_pf(self, t):
        for i in range(t.block.shape[0]):
            for j in range(t.block.shape[1]):
                if t.block[i,j] != 0:
                    self.pf[i+t.r, j+t.c] = t.block[i,j]
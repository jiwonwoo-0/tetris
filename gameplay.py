import numpy as np
import tkinter as tk
from playfield import Playfield
from tetromino import Tetromino
import random
import time

class Tetris: 

    def __init__(self, root, block_size = 30):
        self._color_dict = {0:'white',1:'cyan',2:'blue',3:'orange',4:'yellow',5:'green',6:'purple',7:'red'}
        self.root = root
        self._block_size = block_size
        self.canvas = tk.Canvas(self.root, width=10*self._block_size, height=20*self._block_size)
        self.canvas.pack()

        self.pf = Playfield()
        self.draw_pf()
        self.ts = {0: Tetromino(random.randint(1,7))}
        self.draw_tetromino(len(self.ts)-1)
        self.gravity(len(self.ts)-1)
        

    def draw_pf(self):
        '''creates playfield'''
        # self.canvas.delete("all")
        for i in range(self.pf.pf.shape[0]):
            for j in range(self.pf.pf.shape[1]):
                self.canvas.create_rectangle(j * self._block_size, i * self._block_size, (j + 1) * self._block_size, (i + 1) * self._block_size, fill=self._color_dict[self.pf.pf[i,j]])

    def draw_tetromino(self, key):
        t = self.ts[key]
        tags = [key+0.1*i for i in range(4)]
        idx = 0
        for tag in tags:
            self.canvas.delete(tag)
        for i in range(t.block.shape[0]):
            for j in range(t.block.shape[1]):
                if t.block[i,j] != 0:
                    self.canvas.create_rectangle((j+t.c) * self._block_size, 
                                                 (i+t.r) * self._block_size, 
                                                 ((j+t.c) + 1) * self._block_size, 
                                                 ((i+t.r)+ 1) * self._block_size, 
                                                 fill=self._color_dict[t.block[i,j]], tags=tags[idx])
                    idx +=1

    def gravity(self, key):
        ''
        if self.check_pf(self.ts[key]): #add or hits solid
            self.draw_tetromino(key)
            self.root.after(500, lambda: self.gravity(key))
            self.ts[key].r += 1
        else: 
            self.pf.update_pf(self.ts[key])
            self.draw_pf()
            self.ts[key+1] = Tetromino(random.randint(1, 7))
            self.draw_tetromino(key+1)
            self.root.after(500, lambda: self.gravity(key+1))
    
    def check_pf(self, t):
        if t.r + t.block.shape[0] >= 20:
            return False
        for i in range(t.block.shape[0]):
            for j in range(t.block.shape[1]):
                if (t.block[i,j] != 0) and (self.pf.pf[i+t.r+1, j+t.c] != 0):
                    return False
        return True
        


if __name__ == "__main__":
    root = tk.Tk()
    tetris = Tetris(root)
    root.mainloop()
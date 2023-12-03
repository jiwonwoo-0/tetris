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
        self.tags = ['a','b','c','d']
        self.pf_tags = []
        self.pf = Playfield()
        self.draw_pf()
        
        self.t = Tetromino(random.randint(1,7))
        
        self.draw_tetromino()
        self.gravity()

        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Up>", self.rotate_t)
        self.root.bind("<Down>", self.down)
        

    def draw_pf(self):
        '''creates playfield'''
        for tag in self.pf_tags:
            self.canvas.delete(tag)
            print(tag)
        self.pf_tags = []
        for i in range(self.pf.pf.shape[0]):
            for j in range(self.pf.pf.shape[1]):
                if self.pf.pf[i,j] != 0:
                    self.pf_tags.append('pf'+str(len(self.pf_tags)))
                    self.canvas.create_rectangle(j * self._block_size, i * self._block_size, (j + 1) * self._block_size, (i + 1) * self._block_size, fill=self._color_dict[self.pf.pf[i,j]], tags = self.pf_tags[-1])

    def draw_tetromino(self):
        idx = 0
        for tag in self.tags:
            self.canvas.delete(tag)
        for i in range(self.t.block.shape[0]):
            for j in range(self.t.block.shape[1]):
                if self.t.block[i,j] != 0:
                    self.canvas.create_rectangle((j+self.t.c) * self._block_size, 
                                                 (i+self.t.r) * self._block_size, 
                                                 ((j+self.t.c) + 1) * self._block_size, 
                                                 ((i+self.t.r)+ 1) * self._block_size, 
                                                 fill=self._color_dict[self.t.block[i,j]], tags=self.tags[idx])
                    idx +=1
        self.check_line_clear()

    def gravity(self):
        ''
        self.t.r += 1
        if self.check_edge() and self.check_hit(): #add or hits solid
            self.draw_tetromino()
            self.root.after(500, lambda: self.gravity())
        else:
            self.t.r -= 1
            self.pf.add_t(self.t)
            self.draw_pf()
            self.t = Tetromino(random.randint(1, 7))
            self.draw_tetromino()
            self.root.after(500, lambda: self.gravity())
    
    def check_edge(self):
        if self.t.r + self.t.block.shape[0] >= 21:
            return False
        if (self.t.c < 0) or (self.t.c + self.t.block.shape[1]) > 10:
            return False
        return True
    
    def check_hit(self):
        for i in range(self.t.block.shape[0]):
            for j in range(self.t.block.shape[1]):
                if (self.t.block[i,j] != 0) and (self.pf.pf[i+self.t.r, j+self.t.c] != 0):
                    return False
        return True
    
    def left(self, event):
        self.t.c -= 1
        if self.check_edge() and self.check_hit():
            self.draw_tetromino()
        else:
            self.t.c += 1

    def right(self, event):
        self.t.c += 1
        if self.check_edge() and self.check_hit():
            self.draw_tetromino()
        else:
            self.t.c -= 1
    
    def down(self, event):
        self.t.r += 1
        if self.check_edge() and self.check_hit():
            self.draw_tetromino()
        else:
            self.t.r -= 1
    
    def rotate_t(self, event):
        self.t.rotate()
        if self.check_edge() and self.check_hit():
                self.draw_tetromino()
        else: 
            self.t.rotate(-1)
    
    def check_line_clear(self):
        clear_line = []
        for i, row in enumerate(self.pf.pf):
            if np.count_nonzero(row) == 10:
                clear_line.append(i)
        for line in clear_line: 
            print(line)           
            self.pf.clear_line(line)
            self.draw_pf()




if __name__ == "__main__":
    root = tk.Tk()
    tetris = Tetris(root)
    root.mainloop()
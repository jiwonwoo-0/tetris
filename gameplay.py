import numpy as np
import tkinter as tk
from playfield import Playfield
from tetromino import Tetromino
import random
import time

class Tetris: 

    def __init__(self, root, block_size = 30):
        self._color_dict = {-1: 'black', 0:'white',1:'cyan',2:'blue',3:'orange',4:'yellow',5:'green',6:'purple',7:'red'}
        self.root = root
        self._block_size = block_size
        self.lines = 0
        self.level = 1
        self.score = 0
        self.endgame = False
        self.score_dict = {1:100,2:300,3:500,4:800}
        self.canvas = tk.Canvas(self.root, width=10*self._block_size, height=20*self._block_size)
        self.line_label = tk.Label(self.root, text="Lines: 0")
        self.line_label.pack(side="top")

        self.level_label = tk.Label(self.root, text="Level: 1")
        self.level_label.pack(side="top")

        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack(side="top")
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
        self.line_label.config(text=f"Lines: {self.lines}")
        self.level_label.config(text=f"Level: {self.level}")
        self.score_label.config(text=f"Score: {self.score}")
        if sum(self.pf.pf[0]) != 0:
            self.endgame = True
            self.pf.game_over()
            for i in range(self.pf.pf.shape[0]):
                for j in range(self.pf.pf.shape[1]):
                    self.canvas.create_rectangle(j * self._block_size /2, i * self._block_size/2, (j + 1) * self._block_size/2, (i + 1) * self._block_size/2, fill=self._color_dict[self.pf.pf[i,j]])
            return
        for tag in self.pf_tags:
            self.canvas.delete(tag)
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
        if not self.endgame: 
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
            self.root.after(int(500/self.level), lambda: self.gravity())
        else:
            self.t.r -= 1
            self.pf.add_t(self.t)
            self.draw_pf()
            self.t = Tetromino(random.randint(1, 7))
            self.draw_tetromino()
            self.root.after(int(500/self.level), lambda: self.gravity())
    
    def check_edge(self):
        if self.endgame: return False
        if self.t.r + self.t.block.shape[0] > 20:
            return False
        if (self.t.c < 0) or (self.t.c + self.t.block.shape[1]) > 10:
            return False
        return True
    
    def check_hit(self):
        if self.endgame: return False
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
        lines = []
        for i, row in enumerate(self.pf.pf):
            if np.count_nonzero(row) == 10:
                lines.append(i)
        if len(lines) != 0: 
            self.lines += len(lines)
            self.score += self.score_dict[len(lines)] * self.level
            if self.lines >= self.level * 10:
                self.level += 1
            self.pf.clear_line(lines)
            self.draw_pf()


if __name__ == "__main__":
    root = tk.Tk()
    tetris = Tetris(root)
    root.mainloop()
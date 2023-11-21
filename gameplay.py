import numpy as np
import tkinter as tk
from playfield import Playfield

class Tetris: 

    def __init__(self, block_size = 30):
        self._color_dict = {0:'white',1: 'cyan',2:'blue',3:'orange',4:'yellow',5:'green',6:'purple',7:'red'}
        self.root = tk.Tk()
        self._block_size = block_size
        self.canvas = tk.Canvas(self.root, width=10*self._block_size, height=20*self._block_size)
        self.canvas.pack()
        self.pf = Playfield()
        self.draw_pf()

        self.root.mainloop()

    def draw_pf(self):
        '''creates playfield'''
        self.canvas.delete("all")
        for i in range(self.pf.pf.shape[0]):
            for j in range(self.pf.pf.shape[1]):
                self.canvas.create_rectangle(j * self._block_size, i * self._block_size, (j + 1) * self._block_size, (i + 1) * self._block_size, fill=self._color_dict[self.pf.pf[i,j]])


if __name__ == "__main__":
    tetris = Tetris()
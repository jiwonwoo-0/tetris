import numpy as np

class Sandtris_Playfield:
    """
    Playfield grid for tetris game

    Attributes:
        pf (numpy.ndarray): 2D array representing the playfield
    """

    def __init__(self, scale =3):
        """
        Initializes the Playfield with an empty 20x10 grid
        """
        self.scale = scale
        self.pf = np.zeros((20*scale, 10*scale))
    
    def add_t(self, t):
        """
        Adds a Tetromino to the playfield

        Parameters:
            t (Tetromino): Tetromino added to playfield
        """
        for i in range(t.block.shape[0]):
            for j in range(t.block.shape[1]):
                if t.block[i,j] != 0:
                    self.pf[i+t.r, j+t.c] = t.block[i,j]
    
    def gaps(self):
        orig_pf = self.pf.copy()
        for col in range(self.pf.shape[1]): 
            arr = self.pf[:,col]
            arr = arr[np.argmax(arr != 0):] if np.any(arr != 0) else np.array([])
            zero_ind = np.where(arr == 0)[0]
            arr = np.delete(arr, zero_ind[0]) if len(zero_ind) > 0 else arr
            new_col = np.pad(arr, (self.pf.shape[0] - len(arr), 0), 'constant')
            self.pf[:,col] = new_col
        return np.array_equal(orig_pf, self.pf)
    
    def gaps(self):
        orig_pf = self.pf.copy()
        for col in range(self.pf.shape[1]): 
            arr = self.pf[:,col]
            arr = arr[np.argmax(arr != 0):] if np.any(arr != 0) else np.array([])
            zero_ind = np.where(arr == 0)[0]
            arr = np.delete(arr, zero_ind[0]) if len(zero_ind) > 0 else arr
            new_col = np.pad(arr, (self.pf.shape[0] - len(arr), 0), 'constant')
            self.pf[:,col] = new_col
        return np.array_equal(orig_pf, self.pf)

    def gravity(self):
        orig_pf = self.pf.copy()
        for col in range(self.pf.shape[1]): 
            non_zeros = self.pf[np.nonzero(self.pf[:, col])][:, col]
            neighbors = {}
            neighbors[1] = len(non_zeros) - np.count_nonzero(self.pf[:,col+1]) if col + 1 < self.pf.shape[1] else 0
            neighbors[-1] = len(non_zeros) - np.count_nonzero(self.pf[:,col-1]) if col - 1 >= 0 else 0
            max_diff = max(neighbors, key=neighbors.get)
            if neighbors[max_diff] > 1:
                new_neighbor = np.insert(self.pf[np.nonzero(self.pf[:, col+max_diff])][:, col+max_diff], 0, non_zeros[0])
                new_neighbor = np.pad(new_neighbor, (self.pf.shape[0] - len(new_neighbor), 0), 'constant')
                new_col = np.delete(non_zeros, 0)
                new_col = np.pad(new_col, (self.pf.shape[0] - len(new_col), 0), 'constant')
                self.pf[:,col] = new_col
                self.pf[:,col+max_diff] = new_neighbor
        return ~np.array_equal(orig_pf, self.pf)    
    
    def clear_line(self, rows):
        """
        Deletes lines from playfield

        Parameters:
            rows (list): List of row indices to be deleted
        """
        self.pf = np.delete(self.pf, rows, 0)
        self.pf = np.insert(self.pf, np.zeros_like(rows), np.zeros(10), 0)

    def game_over(self):
        """
        Replaces playfield with game over screen
        """
        self.pf = np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1, 1, 1, 1,-1,-1, 2, 2, 2,-1, 3,-1,-1,-1, 3, 4, 4, 4, 4, 4],
                        [ 1,-1,-1,-1, 1, 2,-1,-1,-1, 2, 3, 3,-1, 3, 3, 4,-1,-1,-1,-1],
                        [ 1,-1,-1,-1,-1, 2,-1,-1,-1, 2, 3,-1, 3,-1, 3, 4,-1,-1,-1,-1],
                        [ 1,-1,-1,-1,-1, 2, 2, 2, 2, 2, 3,-1,-1,-1, 3, 4, 4, 4,-1,-1],
                        [ 1,-1,-1, 1, 1, 2,-1,-1,-1, 2, 3,-1,-1,-1, 3, 4,-1,-1,-1,-1],
                        [ 1,-1,-1,-1, 1, 2,-1,-1,-1, 2, 3,-1,-1,-1, 3, 4,-1,-1,-1,-1],
                        [-1, 1, 1, 1,-1, 2,-1,-1,-1, 2, 3,-1,-1,-1, 3, 4, 4, 4, 4, 4],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1, 5, 5, 5,-1, 6,-1,-1,-1, 6, 7, 7, 7, 7, 7,-1, 1, 1, 1,-1],
                        [ 5,-1,-1,-1, 5, 6,-1,-1,-1, 6, 7,-1,-1,-1,-1, 1,-1,-1,-1, 1],
                        [ 5,-1,-1,-1, 5, 6,-1,-1,-1, 6, 7,-1,-1,-1,-1, 1,-1,-1,-1, 1],
                        [ 5,-1,-1,-1, 5, 6,-1,-1,-1, 6, 7, 7, 7,-1,-1, 1, 1, 1, 1,-1],
                        [ 5,-1,-1,-1, 5, 6,-1,-1,-1, 6, 7,-1,-1,-1,-1, 1,-1, 1,-1,-1],
                        [ 5,-1,-1,-1, 5,-1, 6,-1, 6,-1, 7,-1,-1,-1,-1, 1,-1,-1, 1,-1],
                        [-1, 5, 5, 5,-1,-1,-1, 6,-1,-1, 7, 7, 7, 7, 7, 1,-1,-1,-1, 1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        ])
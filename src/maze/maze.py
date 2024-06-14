from .cell import Cell
import time
import random

class Maze:
    def __init__(self,
                 x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()

    def create_cells(self):
        self.cells = [[Cell(self.win) for i in range(self.num_cols)] for i in range(self.num_rows)]
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.draw_cell(i , j)
        
    def draw_cell(self, i, j):
        self.cells[i][j].draw(self.x1 * j, self.y1 * i,
                               self.cell_size_x * (j + 1), self.cell_size_y * (i + 1))
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.01)
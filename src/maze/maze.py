from .cell import Cell
import time
import random

class Maze:
    def __init__(self,
                 x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win = None,
                 seed = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if not seed is None:
            random.seed(seed)
        self.create_cells()

    def create_cells(self):
        self.cells = [[Cell(self.win) for j in range(self.num_rows)] for i in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i , j)
        
    def draw_cell(self, i, j):
        if self.win is None:
            return
        _x1 = self.x1 + i * self.cell_size_x
        _y1 = self.y1 + j * self.cell_size_y
        self.cells[i][j].draw(_x1, _y1, self.cell_size_x + _x1, self.cell_size_y + _y1)
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.01)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls(self, i, j):
        self.cells[i][j].visited = True

        while True:
            to_visit = []

            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self.draw_cell(i, j)
                return
            
            new_direct = random.randrange(len(to_visit))
            next_cell_ind = to_visit[new_direct]

            if next_cell_ind[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            if next_cell_ind[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i - 1][j].has_left_wall = False
            if next_cell_ind[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False
            if next_cell_ind[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            self.break_walls(next_cell_ind[0], next_cell_ind[1])    
    
    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i < self.num_cols - 1 and not self.cells[i][j].has_right_wall and not self.cells[i + 1][j].visited:
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self.solve_r(i + 1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)
        if j < self.num_rows - 1 and not self.cells[i][j].has_bottom_wall and not self.cells[i][j + 1].visited:
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self.solve_r(i, j + 1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)
        if i > 0 and not self.cells[i][j].has_left_wall and not self.cells[i - 1][j].visited:
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self.solve_r(i - 1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)
        if j > 0 and not self.cells[i][j].has_top_wall and not self.cells[i][j - 1].visited:
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self.solve_r(i, j - 1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)
        return False
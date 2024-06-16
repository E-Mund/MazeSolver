from src.gui.window import Window
from src.maze.cell import Cell
from src.maze.maze import Maze

def main():
    win = Window(600, 400)

    build_maze(win)

    win.wait_for_close()

def build_maze(win):
    maze = Maze(0, 00, 20, 20, win.width // 20, win.height // 20, win)
    maze.create_cells()
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()
    maze.solve()

if __name__ == "__main__":
    main()

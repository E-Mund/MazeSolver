from src.gui.window import Window
from src.maze.cell import Cell
from src.maze.maze import Maze

def main():
    win = Window(800, 600)

    build_maze(win)

    win.wait_for_close()

def build_maze(win):
    maze = Maze(40, 40, 10, 20, win.width // 40, win.height // 40, win, 0)
    maze.create_cells()
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()

if __name__ == "__main__":
    main()

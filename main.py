from src.gui.window import Window
from src.maze.cell import Cell
from src.maze.maze import Maze

def main():
    win = Window(800, 600)

    build_maze(win)

    win.wait_for_close()

def build_maze(win):
    maze = Maze(0, 0, 20, 20, win.width // 20, win.height // 20, win)
    maze.create_cells()

if __name__ == "__main__":
    main()

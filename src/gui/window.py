from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width) -> None:
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, height=height, width=width, background='white')
        self.canvas.pack()
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning == True:
            self.redraw()

    def close(self):
        self.isRunning = False
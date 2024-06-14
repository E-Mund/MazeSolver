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

    def draw_line(self, line, fill_color="black"):
        line.draw(fill_color=fill_color)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )
from gui.window import *

def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(400, 300))
    line.draw(win.canvas, "red")
    win.wait_for_close()

if __name__=="__main__":
    main()

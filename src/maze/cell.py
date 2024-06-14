from ..gui.window import Line, Point

class Cell:
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall == True:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall == True:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall == True:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall == True:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        
    def draw_move(self, to_cell, undo=False):
        if undo == False:
            cur_center = Point(abs((self._x1 + self._x2) // 2), abs((self._y1 + self._y2) // 2))
            to_center = Point(abs((to_cell._x1 + to_cell._x2) // 2), abs((to_cell._y1 + to_cell._y2) // 2))
            line = Line(cur_center, to_center)
            self._win.draw_line(line, "red")
        else:
            cur_center = Point(abs((self._x1 + self._x2) // 2), abs((self._y1 + self._y2) // 2))
            to_center = Point(abs((to_cell._x1 + to_cell._x2) // 2), abs((to_cell._y1 + to_cell._y2) // 2))
            line = Line(cur_center, to_center)
            self._win.draw_line(line, "gray")
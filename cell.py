import time

from point import Point
from line import Line
from window import Window


class Cell:

    def __init__(self,
                 win: Window | None,
                 point1: Point = Point(-1, -1),
                 point2: Point = Point(-1, -1),
                 fill_color: str = "black",
                 clear_color: str = "#d9d9d9",
                 width: float = 2.0,
                 exit: bool = False) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        self.fill_color = fill_color
        self.clear_color = clear_color
        self.width = width
        self.visited = False
        self.exit = exit
        self.__xy1 = point1
        self.__xy2 = point2
        self.__win = win

    def center(self) -> Point:
        return Point((self.__xy1.x + self.__xy2.x) / 2.0,
                     (self.__xy1.y + self.__xy2.y) / 2.0)

    def draw(self) -> None:
        topleft = self.__xy1
        topright = Point(self.__xy2.x, self.__xy1.y)
        botleft = Point(self.__xy1.x, self.__xy2.y)
        botright = self.__xy2

        # Left
        Line(self.__win, topleft, botleft,
             self.fill_color if self.has_left_wall else self.clear_color,
             self.width).draw()

        # Top
        Line(self.__win, topleft, topright,
             self.fill_color if self.has_top_wall else self.clear_color,
             self.width).draw()

        # Right
        Line(self.__win, topright, botright,
             self.fill_color if self.has_right_wall else self.clear_color,
             self.width).draw()

        # Bottom
        Line(self.__win, botleft, botright,
             self.fill_color if self.has_bot_wall else self.clear_color,
             self.width).draw()

    def draw_move(self,
                  to_cell: Cell,
                  undo: bool = False,
                  delay: float = 0.0) -> None:
        Line(self.__win, self.center(), to_cell.center(),
             "#bababa" if undo else "red").draw()
        if delay:
            self.__win.redraw()
            time.sleep(delay)

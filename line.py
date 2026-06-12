from point import Point
from window import Window


class Line:

    def __init__(self,
                 win: Window | None,
                 point1: Point,
                 point2: Point,
                 fill_color: str = "black",
                 width: float = 5.0) -> None:
        self.__win = win
        self.point1 = point1
        self.point2 = point2
        self.fill_color = fill_color
        self.width = width

    def draw(self) -> None:
        if self.__win is None:
            return
        self.__win.canvas.create_line(self.point1.x,
                                      self.point1.y,
                                      self.point2.x,
                                      self.point2.y,
                                      fill=self.fill_color,
                                      width=self.width)

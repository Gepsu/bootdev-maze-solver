class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __mul__(self, other) -> Point:
        if isinstance(other, float) or isinstance(other, int):
            return Point(self.x * other, self.y * other)
        elif isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return NotImplemented

    def __rmul__(self, other) -> Point:
        return self.__mul__(other)

    def __add__(self, other) -> Point:
        if isinstance(other, float) or isinstance(other, int):
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

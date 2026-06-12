import random
from tkinter import Canvas
from typing import List, Tuple

from cell import Cell
from point import Point
from window import Window


class Maze:

    def __init__(self,
                 win: Window | None,
                 x: int,
                 y: int,
                 rows: int,
                 cols: int,
                 cell_size: float,
                 cell_color: str = "black",
                 line_width=2.0,
                 seed=None) -> None:
        self.__win = win
        self.x = x
        self.y = y
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cell_color = cell_color
        self.line_width = line_width
        self.__cells: List[List[Cell]] = []

        random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r()
        self.__reset_cells_visited()

    def __create_cells(self) -> None:
        start = Point(self.x, self.y)
        for x in range(self.rows):
            current_row = []
            for y in range(self.cols):
                pos = Point(x, y)
                topleft = start + pos * self.cell_size
                botright = topleft + Point(self.cell_size, self.cell_size)
                cell = Cell(self.__win,
                            topleft,
                            botright,
                            self.cell_color,
                            width=self.line_width)
                current_row.append(cell)
            self.__cells.append(current_row)
        self.__cells[self.rows - 1][self.cols - 1].exit = True

    def __break_entrance_and_exit(self) -> None:
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        entrance.draw()
        exit = self.__cells[self.rows - 1][self.cols - 1]
        exit.has_bot_wall = False
        exit.draw()

    def __break_walls_r(self, x: int = 0, y: int = 0) -> None:
        can_visit: List[Tuple[int, int, str, str]] = []

        cell = self.__cells[x][y]
        cell.visited = True

        if x - 1 >= 0:
            left = self.__cells[x - 1][y]
            if not left.visited:
                can_visit.append((x - 1, y, "has_left_wall", "has_right_wall"))

        if y - 1 >= 0:
            top = self.__cells[x][y - 1]
            if not top.visited:
                can_visit.append((x, y - 1, "has_top_wall", "has_bot_wall"))

        if x + 1 < self.rows:
            right = self.__cells[x + 1][y]
            if not right.visited:
                can_visit.append((x + 1, y, "has_right_wall", "has_left_wall"))

        if y + 1 < self.cols:
            bot = self.__cells[x][y + 1]
            if not bot.visited:
                can_visit.append((x, y + 1, "has_bot_wall", "has_top_wall"))

        while can_visit:
            i, j, din, dout = can_visit.pop(
                random.randint(0,
                               len(can_visit) - 1))
            next_cell = self.__cells[i][j]
            if next_cell.visited:
                continue
            setattr(cell, din, False)
            setattr(next_cell, dout, False)
            next_cell.draw()
            self.__break_walls_r(i, j)

    def __reset_cells_visited(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                self.__cells[x][y].visited = False

    def __solve_r(self, x: int = 0, y: int = 0) -> bool:
        can_visit: List[Tuple[int, int]] = []
        cell = self.__cells[x][y]
        cell.visited = True

        if cell.exit:
            return True

        if not cell.has_left_wall:
            left = self.__cells[x - 1][y]
            if not left.has_right_wall and not left.visited:
                can_visit.append((x - 1, y))

        if not cell.has_top_wall:
            top = self.__cells[x][y - 1]
            if not top.has_bot_wall and not top.visited:
                can_visit.append((x, y - 1))

        if not cell.has_right_wall:
            right = self.__cells[x + 1][y]
            if not right.has_left_wall and not right.visited:
                can_visit.append((x + 1, y))

        if not cell.has_bot_wall:
            bot = self.__cells[x][y + 1]
            if not bot.has_top_wall and not bot.visited:
                can_visit.append((x, y + 1))

        while can_visit:
            i, j = can_visit.pop(random.randint(0, len(can_visit) - 1))
            next_cell = self.__cells[i][j]
            if next_cell.visited:
                continue
            cell.draw_move(next_cell, delay=0.05)
            if self.__solve_r(i, j):
                return True
            cell.draw_move(next_cell, True, 0.05)

        return False

    def solve(self) -> None:
        self.__solve_r()

    def draw(self) -> None:
        for x in range(self.rows):
            for y in range(self.cols):
                self.__cells[x][y].draw()

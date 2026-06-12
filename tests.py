import unittest

from maze import Maze


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        maze = Maze(None, 0, 0, rows, cols, 32)
        self.assertEqual(len(maze._Maze__cells), rows)
        self.assertEqual(len(maze._Maze__cells[0]), cols)

    def test_maze_reset(self):
        cols = 12
        rows = 10
        maze = Maze(None, 0, 0, rows, cols, 32)
        for x in range(rows - 1):
            for y in range(cols - 1):
                self.assertFalse(maze._Maze__cells[x][y].visited)


if __name__ == "__main__":
    unittest.main()

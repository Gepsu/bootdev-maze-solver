from maze import Maze
from window import Window

if __name__ == "__main__":
    win = Window(800, 800, "Boot.dev Maze Solver")

    maze = Maze(win, 20, 20, 12, 12, 64, "gray", 5.0)
    maze.solve()

    win.wait_for_close()

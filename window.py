from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width: int, height: int, title: str = "") -> None:
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

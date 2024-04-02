import ttkbootstrap as ttk


class App(ttk.Window):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+800+400")
        self.minsize(size[0], size[1])


App("Understanding tkinter lay", (600, 600))

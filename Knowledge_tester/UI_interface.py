import tkinter

import Knowledge_tester.Core


class Window:

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('Тестировщик знаний')
        self.win.geometry("800x600+200+300")  # параметры окна + удаленость от верхнего левого угла
        self.win.minsize(400, 400)
        self.win.mainloop()



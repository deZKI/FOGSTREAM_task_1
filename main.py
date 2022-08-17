from tkinter import Tk
from Knowledge_tester.UI_interface import Example

# pip install lxml
# pip install requests
# pip install bs4

if __name__ == "__main__":
    # test = Test()
    root = Tk()
    root.title('Тестировщик знаний')
    root.geometry("850x550+300+300")
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()
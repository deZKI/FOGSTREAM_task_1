from tkinter import Tk
from Knowledge_tester.UI_interface import Example
from functools import reduce
import requests
# pip install lxml
# pip install requests
# pip install bs4

if __name__ == "__main__":
    # img = requests.get('https://konstruktortestov.ru/files/2b58/1136/8fe2/71f8/bc8b/1f4b/ab0f/3729/904052167.jpg')
    # out = open('1.jpeg', 'wb')
    # out.write(img.content)
    # out.close()
    root = Tk()
    root.title('Тестировщик знаний')
    root.geometry("850x650+300+300")
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()
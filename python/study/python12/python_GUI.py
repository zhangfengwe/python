# GUI

from tkinter import Tk
from tkinter import Button
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import Entry

def load():
    with open(filename.get(),encoding='utf-8') as file:
        contents.delete('1.0', tkinter.END)
        contents.insert(tkinter.INSERT, file.read())

def save():
    with open(filename.get(), 'w',encoding='utf-8') as file:
        file.write(contents.get('1.0', tkinter.END))

top = Tk()
top.title = 'GUI_test'

contents = ScrolledText()
contents.pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.BOTH)
filename = Entry()
filename.pack(side=tkinter.LEFT, expand=True, fill=tkinter.X)
Button(text='Open', command=load).pack(side=tkinter.LEFT)
Button(text='Save', command=save).pack(side=tkinter.LEFT)
tkinter.mainloop()


# def main():
#
#
# if __name__ == '__main__':
#     main()
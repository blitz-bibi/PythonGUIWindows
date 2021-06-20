from tkinter import *
import tkinter

windows = Tk() #instantiate an instance of a windows

#window is an instance of Tkinter's TK class


windows.geometry("500x500")

windows.title("G U I program")

greeting = tkinter.Label(text="Hello, Tkinter")

greeting.pack()

windows.mainloop()
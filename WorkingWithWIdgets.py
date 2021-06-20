from tkinter import *
import tkinter

windows = Tk()

windows.geometry("500x500")

windows.title("Widgets ")

label = Tk.Label(text="Hello, Tkinter")

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

label = tkinter.Label(text="Hello, Tkinter", background="#34A2FE")

label = tkinter.Label(text="Hello, Tkinter", fg="white", bg="black")

label = tkinter.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

button = tkinter.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = TK.Entry(fg="yellow", bg="blue", width=50)


windows.config(background='orange')

#windows.iconphoto(True, icon)

windows.mainloop()
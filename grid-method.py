from tkinter import *

parent = Tk()

name = Label(parent,text = "Name").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1)  
password = Label(parent,text = "Password").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit").grid(row = 12, column = 0)  
# window.title("Hello world")
# window.geometry("300x300")

# hello = tk.Label(text="Hello world!")
# hello.pack()
# button = tk.Button(text="Click me!")
# button.pack()
# tk.mainloop()
parent.mainloop()

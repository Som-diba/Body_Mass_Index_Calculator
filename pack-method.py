from tkinter import *

window = Tk()

redbutton = Button(window, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  
greenbutton = Button(window, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
bluebutton = Button(window, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
blackbutton = Button(window, text = "Green", fg = "red")  
blackbutton.pack( side = BOTTOM)  
# window.title("Hello world")
# window.geometry("300x300")

# hello = tk.Label(text="Hello world!")
# hello.pack()
# button = tk.Button(text="Click me!")
# button.pack()
# tk.mainloop()
window.mainloop()
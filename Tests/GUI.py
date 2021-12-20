from tkinter import *
from tkinter import ttk

def _button_():
    value = entry.get()


main_w = Tk()

main_w.title("Main Window")
main_w.geometry("400x300")

button = ttk.Button(text="Button")
button.pack()
entry = ttk.Entry()
entry.pack()
label = ttk.Label(text="Label ttk")
label.pack()


button1 = Button(text="Button")
button1.pack()
entry1 = Entry()
entry1.pack()
label1 = Label(text="Label")
label1.pack()









main_w.mainloop()

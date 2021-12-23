from tkinter import *

root = Tk()
root.resizable(0, 0)
root.title('CAPITALIZE')


def capitalize():
    global out
    input = text1.get("1.0", END)
    text1.delete("1.0", END)
    out = input.upper()
    text1.insert("1.0", out)


text1 = Text(root, font=('arial', 40, 'bold'), height=3, width=15)
text1.pack()

button1 = Button(root, text="CAPITALIZE", font=('arial', 40, 'bold'), command=capitalize)
button1.pack()
root.mainloop()

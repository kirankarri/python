import tkinter

screen = tkinter.Tk()
screen.title('This is my first GUI')
screen.minsize(width=300,height=500)

label = tkinter.Label(text="I am a label")
label.pack()


screen.mainloop()
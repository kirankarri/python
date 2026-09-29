from tkinter import *

screen = Tk()
screen.title('Miles to KMs')
screen.minsize(300,300)

def Miles_to_Kms():
    miles = float(my_input.get())
    my_label_kms.config(text=f'{round(miles*1.609,2)}')

my_input = Entry()
my_input.grid(column=1,row=0)

my_label_miles = Label(text='Miles')
my_label_miles.grid(column=2,row=0)

my_label = Label(text='is equal to')
my_label.grid(column=0,row=1)

my_label_kms = Label()
my_label_kms.grid(column=1,row=1)

my_label_km = Label(text='Km')
my_label_km.grid(column=2,row=1)

my_button = Button(text='Click Me', command=Miles_to_Kms)
my_button.grid(column=1,row=2)

my_button_quit = Button(text='Destroy Me', command=screen.destroy)
my_button_quit.grid(column=4,row=0)



screen.mainloop()
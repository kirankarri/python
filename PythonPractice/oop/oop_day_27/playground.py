from tkinter import *
def add(*args):
    sum = 0 
    for i in args:
        sum += i
    return sum

class Car():
    def __init__(self,**kwargs):
        self.color = kwargs.get('color')
        self.model = kwargs.get('model')

print(add(2,3,4,5))

car = Car()
print(car.model)

def button_clicked():
    print(f'I am clicked')

screen = Tk()
screen.title('This is title of Window')
screen.minsize(500,500)
my_label = Label(text='This is Label text')
my_label.grid(column=0,row=0)

my_label['text'] = 'This is replaced text'
buttonClickTimes = 0
my_button = Button(text='Click Me', command=button_clicked)
my_button.grid(column=2,row=2)

my_button_quit = Button(text='Destroy Me', command=screen.destroy)
my_button_quit.grid(column=4,row=0)

my_input = Entry()
my_input.grid(column=4,row=3)
print(my_input.get())

screen.mainloop()

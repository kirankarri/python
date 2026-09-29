from tkinter import Tk,Canvas,PhotoImage,Button
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
words = pandas.read_csv('data/french_words.csv')
words_dict = words.to_dict(orient='records');
title_text = ''
word_text = ''
current_card = {}
flip_timer = 0

def flashcard():
    global title_text, word_text, current_card
    canvas.itemconfig(canvas_card,image=card_back)
    canvas.itemconfig(title_text,text='English',fill='white')
    canvas.itemconfig(word_text,text=current_card['English'],fill='white')

def generate_random_word():
    global title_text, word_text, current_card,flip_timer
    screen.after_cancel(flip_timer)
    current_card = words_dict[random.choice(range(0,101))]
    canvas.itemconfig(canvas_card,image=card_front)
    canvas.delete(title_text)
    canvas.delete(word_text)
    title_text=canvas.create_text(400,150,text='French',font=('Arial',40,'italic'),fill='black')
    word_text=canvas.create_text(400,300,text=current_card['French'],font=('Arial',60,'bold'),fill='black')
    flip_timer = screen.after(3000,flashcard)

screen = Tk()
screen.title('Flash Card')
screen.config(padx=10,pady=10,bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000,flashcard)

canvas = Canvas(width=800,height=526)
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas_card = canvas.create_image(400,263,image=card_front)
title_text = canvas.create_text(400,150,text='Title',font=('Arial',40,'italic'),fill='black')
word_text = canvas.create_text(400,300,text='Word',font=('Arial',60,'bold'),fill='black')

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_button = Button(image=wrong,command=generate_random_word)
wrong_button.grid(row=1,column=0)


right_button = Button(image=right,command=generate_random_word)
right_button.grid(row=1,column=1)

generate_random_word()






screen.mainloop()

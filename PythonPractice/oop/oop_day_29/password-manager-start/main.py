from tkinter import *
from tkinter import messagebox
from random import random,shuffle,choice,randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = ''
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    number_letters = [choice(numbers) for _ in range(randint(2,4))]
    symbols_letters = [choice(symbols) for _ in range(randint(2,4))]

    password_combined = password_letters + number_letters + symbols_letters
    password = ''.join(password_combined)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    print(website)
    print(password)
    new_dict = {website:{
                'username': username,
                'password': password
            }}
    if not website or not  password:
        print('test')
        messagebox.askokcancel(message='Website or password fields are empty')
    else:
        is_ok_save = messagebox.askokcancel(title=website,message=f'Below are the entered details\n UserName: {username}\n Password: {password}\n Is it OK to save ?')

        if is_ok_save:
            try:
                with open("data.json", 'r') as file:
                    read_data = json.load(file)             
            except:
                with open("data.json", 'w') as file:
                    json.dump(new_dict,file,indent=4)
                    #file.write(f'{website} | {username} | {password}\n')
                    website_input.delete(0,END)
                    password_input.delete(0,END)
            else:
                read_data.update(new_dict)
                with open("data.json", 'w') as file:
                    json.dump(read_data,file,indent=4)
                #file.write(f'{website} | {username} | {password}\n')
                website_input.delete(0,END)
                password_input.delete(0,END)

def search():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        website_data = data[website_input.get()]
        messagebox.askokcancel(title=website_input.get(),message=f'Below are the password details\n Password: {website_data['password']}\n')
    except FileNotFoundError:
        messagebox.askokcancel(title=website_input.get(),message='There is no File')
    except KeyError:
        messagebox.askokcancel(title=website_input.get(),message='No details for this website exists')
# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Pass Generator')
screen.config(padx=20,pady=20)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=image)
canvas.grid(row=1,column=2)

label_1 = Label(text='Website')
label_1.grid(row=2,column=1)

label_2 = Label(text='Email/ Username')
label_2.grid(row=3,column=1)

label_3 = Label(text='Password')
label_3.grid(row=4,column=1)

website_input = Entry(width=35)
website_input.grid(row=2,column=2)
website_input.focus()

search = Button(text='Search',width=10,command=search)
search.grid(row=2,column=3,columnspan=2)

username_input = Entry(width=35)
username_input.grid(row=3,column=2,columnspan=2)
username_input.insert(0, "kiran10199@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=4,column=2)

p_generate = Button(text='Generate Password',width=10,command=password_generator)
p_generate.grid(row=4,column=3)

add = Button(text='Add',width=36,command=save_password)
add.grid(row=5,column=2,columnspan=2)

screen.mainloop()
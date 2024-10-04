from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = [choice(letters) for _ in range (randint(8,10))]
    num = [choice(numbers) for _ in range (randint(2,4))]
    sym = [choice(symbols) for _ in range (randint(2,4))]

    main_list = let+num+sym

    shuffle(main_list)
    pas = "".join(main_list)

    password_entry.delete(0,END)
    password_entry.insert(0,pas)
    pyperclip.copy(pas)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    data = {
        web_entry.get():{
            "Email" : email_entry.get(),
            "Password" : password_entry.get()
        }
    }

    if len(web_entry.get()) ==0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="warning",message="Please don't leave any fields empty!")
    else:
        try:
            with open("manager.json","r") as file:
                new_data = json.load(file)

        except FileNotFoundError:
            with open("manager.json","w") as file:
                json.dump(data,file,indent=2)
        else:
            new_data.update(data)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()
def search_button():
    name = web_entry.get()
    try:
        with open("manager.json","r") as file:
            web_search = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if name in web_search:
            saved_email = web_search[name]["Email"]
            saved_password = web_search[name]["Password"]
            messagebox.showinfo(title="Your Credentials",message=f"Email: {saved_email}\nPassword: {saved_password}")
        else:
            messagebox.showerror(title="Warning!",message=f"No details for {name} exists!")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_image)
canvas.grid(row=0,column=0,columnspan=2,pady=3)

#Labels

web = Label(text="Website:",)
web.grid(row=1,column=0,pady=3)

email = Label(text="Email/Username:")
email.grid(row=3,column=0,pady=3)

password = Label(text="Password:")
password.grid(row=4,column=0,pady=3)

#entry

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2,pady=3)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=3,column=1,columnspan=2,pady=3)
email_entry.insert(0,"vimalaroan5@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=4,column=1,padx=20,pady=3)


#button

generate = Button(text="Generate Password",width=30,command=generate_password)
generate.grid(row=5,column=1,pady=3)

add = Button(text="Add",width=30,command=save)
add.grid(row=6,column=1,columnspan=2,pady=3)

search = Button(text="Search",width=30,command=search_button)
search.grid(row=2,column=1,pady=3)














window.mainloop()

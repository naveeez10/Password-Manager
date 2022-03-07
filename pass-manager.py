import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- SEARCHING THROUGH DATA ------------------------------- #

def search_data():
    
    with open("data.json","r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {}
    
    data_list = data.items()
    asked = website_entry.get()
    done = False
    
    for key in data_list:
        if key[0] == asked:
            done = True
            req_username = key[1]['username']
            req_password = key[1]['password']
            break
    
    if done == False:
        messagebox.showwarning(title="Ooops",message=f"No credentials found for {asked}")
    else:
        messagebox.showinfo(title="Credentials",message=f"Your credentials for {asked} are : \n Username : {req_username} \n Password : {req_password}\n")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_entry.delete(0,END)
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    
    password_entry.insert(END,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pressed():
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()

    new_data = {
        website_text : {
            "username" : username_text,
            "password" : password_text,
        }
    }

    if website_text == "" or username_text == "" or password_text == "":
        messagebox.showwarning(title="Invalid Field",message="Please fill all the fields")
        return

    try:
            with open("data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except json.decoder.JSONDecodeError:
                    data = {}
    except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
    else:
            data.update(new_data)
            print(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
    finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    messagebox.showinfo(title="Success",message="Credentials Successfully saved!")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text = "Website")
website_label.grid(row = 1,column=0)

username_label = Label(text = "Username/Email")
username_label.grid(row = 2,column=0)

password_label = Label(text = "Password")
password_label.grid(row = 3,column=0)

website_entry = Entry(width = 17)
website_entry.focus()
website_entry.grid(row = 1,column=1,columnspan=1)

username_entry = Entry(width = 35)
username_entry.insert(END,string="vizkhoja@gmail.com")
username_entry.grid(row = 2,column=1,columnspan=2)

search_butt = Button(text="Search",command=search_data)
search_butt.grid(row=1,column=2)

password_entry = Entry(width = 17)
password_entry.grid(row = 3,column=1,columnspan=1)

gen_butt = Button(text="Generate Password",command=generate_password)
gen_butt.grid(row = 3,column=2,columnspan=1)

add_butt = Button(text = "Add",width=30,command = add_pressed)
add_butt.grid(row=4,column=1,columnspan=2)

window.mainloop()
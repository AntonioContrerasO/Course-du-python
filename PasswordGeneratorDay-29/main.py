from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password():
    entry_password.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    random.shuffle(password_list)

    password = "".join(password_list)  # list to string
    entry_password.insert(END, password)

    messagebox.showinfo(title="No te preocupes tengo todo controlado",
                        message="No debes utiliazar 'ctrl + c', ya lo he hecho por ti.")

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {website: {"email": email, "password": password}}

    if len(entry_password.get()) == 0 or len(entry_website.get()) == 0:
        messagebox.showinfo(title="Warning", message="Please don't let an entry empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Saving
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

def search_password():
    try:
        with open("data.json",mode="r") as file:
            contents = json.load(file)
            if entry_website.get() in contents:
                website = entry_website.get()
                email = contents[website]["email"]
                password = contents[website]["password"]
                messagebox.showinfo(title=website,message=f"email: {email}\n password: {password}")
            else:
                messagebox.showinfo(title="Website not found",message="There's not passwords with that name")
    except:
        messagebox.showinfo(title="Error",message="Info Not Found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(bg="white", pady=20, padx=20)
window.resizable(False,False)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=False)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website: ", font=("Arial", 12, "bold"), bg="white")
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username: ", font=("Arial", 12, "bold"), bg="white")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password: ", font=("Arial", 12, "bold"), bg="white")
label_3.grid(row=3, column=0)

entry_website = Entry(width=32, bd=3)
entry_website.grid(row=1, column=1)
entry_website.focus()

entry_email = Entry(width=55, bd=3)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(END, "tuemailmecaqui@gmail.com")

entry_password = Entry(width=32, bd=3)
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password", font=("Arial", 10, "bold"), command=random_password)
button_generate.grid(row=3, column=2)
print(button_generate.winfo_width())

button_add = Button(text="Add", font=("Arial", 10, "bold"), width=41, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="search", font=("Arial", 10, "bold"),width=16,command=search_password)
button_search.grid(row=1, column=2)

window.mainloop()

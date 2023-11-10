from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please don't leave any of the fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving update data
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving update data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(title="Email and Password", message=f"Email: {data[website]['email']}"
                                                                        f"\nPassword: {data[website]['password']} ")
            else:
                messagebox.showinfo(title="No website found", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 8))
website_label.grid(column=0, row=1)
website_entry = Entry(window, width=30, font=("Arial", 9), bg="white")
website_entry.grid(column=1, row=1, columnspan=2, padx=2, pady=2, sticky="w")
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username: ", font=("Arial", 8))
email_label.grid(column=0, row=2)
email_entry = Entry(window, width=48, font=("Arial", 9), bg="white")
email_entry.grid(column=1, row=2, columnspan=2, padx=2, pady=2, sticky="w")
email_entry.insert(0, "danielbaylon2885@icloud.com")

password_label = Label(text="Password: ", font=("Arial", 8))
password_label.grid(column=0, row=3)
password_entry = Entry(window, width=30, font=("Arial", 9), bg="white")
password_entry.grid(column=1, row=3, columnspan=2, sticky="w", padx=2, pady=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2, padx=2, pady=2)

window.mainloop()















































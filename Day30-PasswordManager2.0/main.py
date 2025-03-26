import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random secure password."""
    
    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
  
    password_list = password_letters + password_numbers + password_symbols

    # Shuffle the password_List to randomize order of characters
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    if len(password_entry.get()) == 0:
        password_entry.insert(END, password)
        print(password)
    else:
        # If entry already has value, entry is deleted prior to displaying new generated password
        password_entry.delete(first=0, last=END)
        password_entry.insert(END, password)
        print(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Get the values in the website, username and password entry fields and save the values to a file. 
    Entry fields are reset to default values after data is added."""

    # Get entry box values and save them to variable for readability
    web = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    saved_site = {
        web: {
            "email": user,
            "password": password
            }
        }

    # Check and make sure that entry fields are not empty
    if len(web) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showwarning(title="Missing data", message="Required data is missing!\nMake sure website, username, and password fields are not empty.")
    
    else:
        try:
            with open("./Day30-PasswordManager2.0/data.json", mode="r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("./Day30-PasswordManager2.0/data.json", mode="w") as data_file:
                json.dump(saved_site, data_file, indent=4)

        else:
            # Update old data with new data
            data.update(saved_site)
            with open("./Day30-PasswordManager2.0/data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            # Clear & reset entry fields
            website_entry.delete(first=0, last=END)
            username_entry.delete(first=0, last=END)
            username_entry.insert(END, "username@example.com")
            password_entry.delete(first=0, last=END)

        print("Data written to data.json and entry fields reset to defaults")
        messagebox.showinfo(title="Success", message="Password saved to data.json file")

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_logo = PhotoImage(file="./Day29-PasswordManager/logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Username entry
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "username@example.com")

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Generate Password button
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
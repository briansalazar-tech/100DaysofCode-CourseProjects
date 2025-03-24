from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Get the values in the website, username and password entry fields and save the values to a file. 
    Entry fields are reset to default values after data is added."""

    # Get entry box values and save them to variable for readability
    web = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    # Write data to a text file
    with open("./Day29-PasswordManager/data.txt", mode="a") as data:
        data.write(f"Website: {web} | Username: {user} | Password: {password}\n")
    
    # Clear & reset entry fields
    website_entry.delete(first=0, last=END)
    username_entry.delete(first=0, last=END)
    username_entry.insert(END, "username@example.com")
    password_entry.delete(first=0, last=END)

    print("Data written to data.txt and entry fields reset to defaults")

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
generate_button = Button(text="Generate")
generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
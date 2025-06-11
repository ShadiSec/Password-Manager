from tkinter import *
from tkinter import messagebox
from saved_passwords import ViewPasswords
import random
import pyperclip
import json
from search import Search

EMAIL = "CHANGE_ME@GMAIL.COM" # Set this to your frequently used email.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    password_entry.delete(0, END) # Clears the password entry field.

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generates a random password by selecting a random range of characters of letters, numbers, and symbols.
    letters_list = [random.choice(letters) for _ in range(random.randint(8,10))] # Creates a list containing between 8 & 10 letters.
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2,4))] # Creates a list containing between 2 & 4 numbers.
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2,4))] # Creates a list containing between 2 & 4 symbols.

    password_list = letters_list + numbers_list + symbols_list # Combines the 3 lists into 1.
    random.shuffle(password_list) # Shuffles the characters in the combined password list.
    password_str = "".join(password_list) # Converts the combined list into a string.

    password_entry.insert(0, password_str) # Inserts the generated password into the password field.
    pyperclip.copy(password_str) # Copies the password to the clipboard.

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    """Saves the login information to the data.json file."""
    # Retrieves the text from the entry boxes.
    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
        "email": username,
        "password": password
        }
    }

    # Checks for empty fields.
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please do not leave any fields empty!")
    else:
        # Confirms the credentials with the user.
        confirm = messagebox.askokcancel(title=website, message=f"Confirm adding these credentials:\n"
                                                                f"Email/Username: {username}\n"
                                                                f"Password: {password}")
        # Checks if the user is okay with the credentials entered.
        if confirm:
            # Adds new data to the json file.
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError: # Will just add the data to a dictionary if the file is not found.
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
            except json.JSONDecodeError: # Handles an error occurring when the json file is empty.
                data = {}
            else:
                # Updates and writes the new data.
                data.update(new_data)

            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)

            # Clear the Website and Password entries from the text boxes.
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Create the main window.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creates an image usable by tkinter.
logo = PhotoImage(file="./logo.png")

# Creates a canvas containing the logo.
canvas = Canvas(window, height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label & Entry Box
website_label = Label(text="Website: ")
website_entry = Entry(width=35)

website_entry.focus() # Starts the program with the cursor in the website entry.

website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")


# Search Button
search_button = Button(text="Search", command=lambda: Search(website_entry.get()))
search_button.grid(column=2, row=1, columnspan=2, sticky="E")


# Email/Username Label & Entry
username_label = Label(text="Email/Username: ")
username_entry = Entry(width=35)
username_entry.insert(0, EMAIL) # Starts the program with a commonly used email.
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2, sticky="W")


# Password Label, Entry, and Button
password_label = Label(text="Password: ")
password_entry = Entry(width=24)
password_button = Button(text="Generate Password", command=random_password)

password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, sticky="W", columnspan=2)
password_button.grid(column=1, row=3, sticky="E", columnspan=2)


# Add Button
add_button = Button(text="Add", width=36, bg="#07BD25", fg="white", command=save_info)
add_button.grid(column=1, row=4, columnspan=2)


# View Credentials Button
def view_passwords():
    ViewPasswords()

credentials_button = Button(text="View Passwords", width=36, command=view_passwords)
credentials_button.grid(column=1, row=5, columnspan=2, pady=15)


# Keep the program running.
window.mainloop()

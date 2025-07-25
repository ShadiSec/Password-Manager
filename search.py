from tkinter import messagebox
import pyperclip
import json

class Search:
    def __init__(self, user_website):
        """Finds the credentials of a given website."""
        try:
            with open(file="data.json", mode="r") as file:
                data_dict = json.load(file)
        except json.JSONDecodeError:
            data_dict = {}
            messagebox.showinfo(title="Oops", message="Trouble accessing the database 'data.json'.")
        except FileNotFoundError:
            data_dict = {}
            messagebox.showinfo(title="Oops", message="The database 'data.json' does not seem to exist.")

        try:
            # Check if the website credentials exist.
            if user_website.title() in data_dict:
                email = data_dict[user_website.title()]["email"]
                password = data_dict[user_website.title()]["password"]

                # Display the credentials to the user.
                messagebox.showinfo(title=f"{user_website.title()} Credentials", message=f"Your password has been copied to the clipboard!\n\n"
                                                                            f"Username/Email: {email}\n"
                                                                            f"Password: {password}\n"
                                                                            )
                # Copy the password to the user's clipboard.
                pyperclip.copy(password)
            else:
                raise KeyError
        except KeyError:
            messagebox.showinfo(title="Oops", message="That websites does not exist in the database.")

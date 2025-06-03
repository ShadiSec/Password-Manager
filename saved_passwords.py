from tkinter import *
import pyperclip

class ViewPasswords:
    def __init__(self):
        top_window = Toplevel() # Creates a new top_window above all other windows.

        # Creates a Frame inside the top Window.
        frame = Frame(top_window)
        frame.grid(column=0, row=0, columnspan=2)

        # Creates the scrollbar
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side="right", fill="y")

        # Creates a listbox.
        list_box = Listbox(frame, yscrollcommand=scroll_bar.set, width=50)
        list_box.pack(side="left", fill="both", expand=True)

        scroll_bar.config(command=list_box.yview)

        # Gets the credentials saved in data.txt
        with open(file="./data.txt", mode="r") as file:
            info_list = [credential.strip("\n") for credential in file.readlines()]

        # Propagates the list_box with the credentials saved.
        for credential in info_list:
            list_box.insert(END, f"{credential}\n")

        def copy_password():
            """Copies the password of the selected credential."""
            selected_index = list_box.curselection()
            # Checks if an item is selected.
            if selected_index:
                selected_text = list_box.get(selected_index[0]) # Gets the text of the selected item.
                pyperclip.copy((selected_text.split("|")[-1]).strip(" ")) # Copies to clipboard the password from the text and removes any spaces.
                print("Password Copied!")

        # Creates a Button to copy the password .
        copy_password_button = Button(frame, text="Copy\nPassword", bg="#07BD25", fg="white", command=copy_password)
        copy_password_button.pack(side="left", fill="y")
        top_window.mainloop()

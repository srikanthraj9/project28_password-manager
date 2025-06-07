from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for _ in range(5):
        password_list.append(random.choice(letters))
    for _ in range(4):
        password_list.append(random.choice(symbols))
    for _ in range(3):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password_2 = ""
    for char in password_list:
        password_2 += char
    return password_2
def generate_password_action():
    new_password = password()
    pass_data.delete(0, END)
    pass_data.insert(0, new_password) # Insert new password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = website.get()
    email_entry = email.get()
    password_entry = pass_data.get()

    if not website_entry or not email_entry or not password_entry:
        messagebox.showwarning(title="Warning", message="Please fill in all fields.")
    else:
        is_okay = messagebox.askokcancel(
            title=website_entry,
            message=f"These are the details:\nEmail: {email_entry}\nPassword: {password_entry}\n\nSave entry?"
        )
        if is_okay:
            with open("datat.txt", "a") as data_file:
                data_file.write(f"{website_entry} | {email_entry} | {password_entry}\n")
            website.delete(0, END)
            pass_data.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

font_name = ("Arial", 12, "bold")

web_text = Label(text="Website:", font=font_name)
web_text.grid(column=0, row=1)

website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
website.focus()

user_name = Label(text="Email/Username:", font=font_name)
user_name.grid(column=0, row=2)
email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)
email.insert(0,"srikanth@gmail.com")

password_label= Label(text="Password:", font=font_name)
password_label.grid(column=0, row=3)
pass_data = Entry(width=21)
pass_data.grid(column=1, row=3)

generate_password = Button(text="Generate Password",command=generate_password_action)
generate_password.grid(column=2, row=3)

add = Button(width=36, text="Add",command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()

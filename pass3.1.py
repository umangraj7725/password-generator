from tkinter import *
import pyperclip # used to copy the generated password to clipboard
import random # used in generating the random password

# initializing the tkinter
root = Tk()
root.title("Password Generator.........by Umang Raj 12018505")


root.geometry("400x400")    # setting the width and height of the gui
root.configure(background ="bisque")
passstr = StringVar()  # declaring a variable of string type (used to store the generated password)

passlen = IntVar()     # declaring a variable of string type (used to store the lenght of password entered by user)

passlen.set(0)    # set the length of the password to zero initially


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate the password 
    
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    
    password = ""     # declaring the empty string

    # loop to generate the random password of the length entered  by the user        
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="Password Generator", font="calibri 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length").pack(pady=3)

# Creating a entry widget to take password length entered by the 
# user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

Label(root, text="Created by Umang Raj").pack(pady=100)
# mainloop() is an infinite loop used to run the application when it's in ready state 
root.mainloop()
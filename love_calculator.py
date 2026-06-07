# Python Tkinter GUI based Love Calculator
from tkinter import *
import random

root = Tk()
root.geometry('400x280')
root.title('Love Calculator 💕')
root.resizable(False, False)

def calculate_love():
    n1 = name1.get().strip()
    n2 = name2.get().strip()

    if not n1 or not n2:
        result.config(text="Please enter both names!", fg="red")
        return

    # Generate a consistent percentage based on names (same names = same result)
    seed = sum(ord(c) for c in (n1 + n2).lower())
    random.seed(seed)
    percentage = random.randint(1, 99)
    random.seed()  # reset seed

    if percentage >= 80:
        msg = "💖 Perfect Match!"
    elif percentage >= 60:
        msg = "💛 Good Compatibility!"
    elif percentage >= 40:
        msg = "💙 Could Work!"
    else:
        msg = "💔 Maybe Just Friends..."

    result.config(text=f"Love Percentage: {percentage}%\n{msg}", fg="hot pink")

# Heading
heading = Label(root, text='💕 Love Calculator 💕', font=('Arial', 16, 'bold'))
heading.pack(pady=10)

# Name 1
slot1 = Label(root, text="Enter Your Name:", font=('Arial', 11))
slot1.pack()
name1 = Entry(root, border=5, font=('Arial', 11), width=25)
name1.pack(pady=4)

# Name 2
slot2 = Label(root, text="Enter Your Partner's Name:", font=('Arial', 11))
slot2.pack()
name2 = Entry(root, border=5, font=('Arial', 11), width=25)
name2.pack(pady=4)

# Button
bt = Button(root, text="Calculate 💕", height=1, width=12,
            font=('Arial', 11), bg='hot pink', fg='white', command=calculate_love)
bt.pack(pady=8)

# Result
result = Label(root, text='Enter names and click Calculate!',
               font=('Arial', 12), fg='gray')
result.pack(pady=6)

root.mainloop()

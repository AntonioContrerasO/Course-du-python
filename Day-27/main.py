import random
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=150)
window.config(pady=25, padx=25)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(row=0, column=2)

kilometers = Label(text="Km", font=("Arial", 12, "bold"))
kilometers.grid(row=1, column=2)

kilometers_value = Label(text="0", font=("Arial", 12, "bold"))
kilometers_value.grid(row=1, column=1)

is_equal_to = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(row=1, column=0)


def calculate():
    value = (float(input_entry.get()) * 1.8) + 32
    kilometers_value.config(text=round(value,2))


button = Button(text="Calculate", font=("Arial", 12, "bold"),command=calculate)
button.grid(row=3, column=1)

input_entry = Entry()
input_entry.grid(row=0, column=1)
input_entry.config(width=10)

window.mainloop()

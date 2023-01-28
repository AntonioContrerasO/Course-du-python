import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas

# ---------------------------Flash logic--------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    print("Old Data")
except:
    data = pandas.read_csv("data/french_words.csv")
    print("New Data")
french_words = data["French"].to_list()
english_words = data["English"].to_list()
choice = random.choice(french_words)
choice_english = english_words[french_words.index(choice)]


def i_know_that_word():
    global data
    should_remove = do_ever()
    french_words.remove(should_remove[0])
    english_words.remove(should_remove[1])
    new_data = {"French":french_words,
                "English":english_words}
    data = pandas.DataFrame(new_data)
    data.to_csv("data/words_to_learn.csv",index=False)


def i_do_not_know_that_word():
    do_ever()


def change_to_english(english_word):
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=english_word)


def change_to_french(french_word):
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=french_word)
    canvas.itemconfig(image, image=card_front)


def do_ever():
    new_choice = random.choice(french_words)
    new_choice_english = english_words[french_words.index(new_choice)]
    change_to_french(new_choice)
    window.after(3000, change_to_english, new_choice_english)
    return new_choice, new_choice_english



# ---------------------------GUI--------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=False, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 290, text=choice, fill="black", font=("Arial", 60, "bold"))
window.after(3000, change_to_english, choice_english)
canvas.grid(row=0, column=0, columnspan=2)

check_image = PhotoImage(file="images/right.png")
green_button = Button(image=check_image, highlightthickness=False, bg=BACKGROUND_COLOR, border=False,
                      command=i_know_that_word)
green_button.grid(row=1, column=1)

check_wrong_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=check_wrong_image, highlightthickness=False, bg=BACKGROUND_COLOR, border=False,
                    command=i_do_not_know_that_word)
red_button.grid(row=1, column=0)

window.mainloop()

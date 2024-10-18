from tkinter import *
from tkinter import PhotoImage
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"

# -----------------get data from csv file-----------------#
try:
    words = pandas.read_csv("data/To_Learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
instant_word_set = {}


def next_card():
    global instant_word_set, flip_timer
    window.after_cancel(flip_timer)
    instant_word_set = choice(words)
    french_word = instant_word_set["French"]
    canvas.itemconfig(canvas_image, image = card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill ="black")
    flip_timer = window.after(3000, flip_card)


# -----------------change language-------------#
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    english_word = instant_word_set["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")

# -----------------remove known words-----------#
def known_word():
    words.remove(instant_word_set)
    data = pandas.DataFrame(words)  # Save remaining words, not just the current one
    data.to_csv("data/To_Learn.csv", index=False)  # Save without the index
    next_card()


# -----------------setup window----------------#
window = Tk()
window.title("Flash_Card_Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


card_back = PhotoImage(file = "images/card_back.png")
card_front= PhotoImage(file = "images/card_front.png")
right_icon= PhotoImage(file = "images/right.png")
wrong_icon = PhotoImage(file = "images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400,263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan = 2)

flip_timer = window.after(3000, flip_card)

right_button = Button(image=right_icon, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_icon, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


next_card()

window.mainloop()
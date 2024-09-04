from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/Irish_Frequency_List_Top100.csv')
    words_to_learn = data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(title_text, text="Irish", fill="black")
    canvas.itemconfig(word_text, text=current_card['Irish'], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def remove_card():
    words_to_learn.remove(current_card)
    print(len(words_to_learn))
    updated_data = pd.DataFrame(words_to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Irish to English Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
correct_image = PhotoImage(file='images/right.png')
incorrect_image = PhotoImage(file='images/wrong.png')
flip_image = PhotoImage(file='images/flip1.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=remove_card)
correct_button.grid(column=1, row=1)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_card)
incorrect_button.grid(column=0, row=1)

known_word_label = Label(text="Remove from Deck", font=("Ariel", 15, "italic"), bg=BACKGROUND_COLOR)
known_word_label.grid(column=1, row=2)
unknown_word_label = Label(text="Keep in Deck", font=("Ariel", 15, "italic"), bg=BACKGROUND_COLOR)
unknown_word_label.grid(column=0, row=2)


next_card()

window.mainloop()


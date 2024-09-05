from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = 'data/words_to_learn.csv'
DEFAULT_WORDS_FILE = 'data/Irish_Frequency_List_Top100.csv'
FRONT_IMAGE = 'images/card_front.png'
BACK_IMAGE = 'images/card_back.png'
CORRECT_IMAGE = 'images/right.png'
INCORRECT_IMAGE = 'images/wrong.png'
RESET_IMAGE = 'images/reset.png'


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Irish to English Flashcards")
        self.root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.words_to_learn = self.load_words()
        self.current_card = {}
        self.flip_timer = None

        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
        self.front_img = PhotoImage(file=FRONT_IMAGE)
        self.back_img = PhotoImage(file=BACK_IMAGE)
        self.card_background = self.canvas.create_image(400, 263, image=self.front_img)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.title_text = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.word_text = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

        self.correct_image = PhotoImage(file=CORRECT_IMAGE)
        self.incorrect_image = PhotoImage(file=INCORRECT_IMAGE)
        self.reset_image = PhotoImage(file=RESET_IMAGE)

        self.correct_button = Button(image=self.correct_image, highlightthickness=0, command=self.remove_card)
        self.correct_button.grid(column=2, row=1)
        self.reset_button = Button(image=self.reset_image, highlightthickness=0, command=self.reset_learning)
        self.reset_button.grid(column=1, row=3)
        self.incorrect_button = Button(image=self.incorrect_image, highlightthickness=0, command=self.next_card)
        self.incorrect_button.grid(column=0, row=1)


        Label(text="Remove card", font=("Ariel", 15, "italic"), bg=BACKGROUND_COLOR).grid(column=2, row=2)
        Label(text="Keep in Deck", font=("Ariel", 15, "italic"), bg=BACKGROUND_COLOR).grid(column=0, row=2)
        Label(text="Reset words list", font=("Ariel", 15, "italic"), bg=BACKGROUND_COLOR).grid(column=1, row=4)

        self.next_card()

    def load_words(self):
        """
        Load the list of words to learn from a CSV file. If the file doesn't exist, load a default list.
        """
        if os.path.exists(DATA_FILE):
            data = pd.read_csv(DATA_FILE)
        else:
            data = pd.read_csv(DEFAULT_WORDS_FILE)
        return data.to_dict(orient="records")

    def next_card(self):
        """
        Display the next flashcard with an Irish word.
        """
        if not self.words_to_learn:
            messagebox.showinfo("Congratulations!", "You've learned all the words!")
            return

        if self.flip_timer:
            self.root.after_cancel(self.flip_timer)

        self.current_card = choice(self.words_to_learn)
        self.canvas.itemconfig(self.title_text, text="Irish", fill="black")
        self.canvas.itemconfig(self.word_text, text=self.current_card['Irish'], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.front_img)
        self.flip_timer = self.root.after(3000, self.flip_card)

    def flip_card(self):
        """
        Flip the flashcard to show the English translation.
        """
        self.canvas.itemconfig(self.title_text, text="English", fill="white")
        self.canvas.itemconfig(self.word_text, text=self.current_card["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.back_img)

    def remove_card(self):
        """
        Remove the current card from the list and save the updated list.
        """
        self.words_to_learn.remove(self.current_card)
        self.save_words()
        self.next_card()

    def save_words(self):
        """
        Save the updated list of words to learn to a CSV file.
        """
        updated_data = pd.DataFrame(self.words_to_learn)
        updated_data.to_csv(DATA_FILE, index=False)

    def reset_learning(self):
        """
        Reset the learning process by reloading the original word list.
        """
        if messagebox.askyesno("Reset", "Do you want to reset your progress?"):
            os.remove(DATA_FILE)
            self.words_to_learn = self.load_words()
            self.next_card()

if __name__ == "__main__":
    window = Tk()
    app = FlashcardApp(window)
    window.mainloop()

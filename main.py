from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Irish to English Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=400, width=400)
front_img = PhotoImage(file='card_front.png')
canvas.create_image(200, 200, image=front_img)
canvas.grid(column=1, row=1)




window.mainloop()


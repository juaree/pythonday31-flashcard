from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words_in_dict = data.to_dict(orient="records")
else:
    words_in_dict = data.to_dict(orient="records")
print(len(words_in_dict))
current_word = ""

def change_to_english():
    global flip_timer, current_word
    en_word = current_word['English']
    canvas.itemconfig(translation_text, text=f"{en_word}", fill='white', font=("Arial", 40, "italic"))
    canvas.itemconfig(language_text, text="English", fill='white', font=("Arial", 48, "bold"))
    canvas.itemconfig(canvas_logo, image=green_logo)

def change_word_wrong():
    global flip_timer, current_word
    current_word = rd.choice(words_in_dict)
    fr_word = current_word['French']
    window.after_cancel(flip_timer)
    canvas.itemconfig(translation_text, text=f"{fr_word}", fill='black', font=("Arial", 40, "italic"))
    canvas.itemconfig(language_text, text=f"French", fill='black', font=("Arial", 48, "bold"))
    canvas.itemconfig(canvas_logo, image=white_logo)
    flip_timer = window.after(3000, change_to_english)

def change_word_right():
    global flip_timer, current_word
    words_in_dict.remove(current_word)
    df = pd.DataFrame.from_dict(words_in_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    change_word_wrong()


# Widgets
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
white_logo = PhotoImage(file="images/card_front.png")
green_logo = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_logo = canvas.create_image(400, 263, image=white_logo, )
language_text = canvas.create_text(400, 150, text="", font=("Arial", 28, "italic"))
translation_text = canvas.create_text(400, 263, text="", font=("Arial", 32, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
flip_timer = window.after(3000, change_to_english)

# Button
wrong_logo = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_logo, highlightthickness=0, command=change_word_wrong)
wrong_btn.grid(column=0, row=1)

right_logo = PhotoImage(file="images/right.png")
right_btn = Button(image=right_logo, highlightthickness=0, command=change_word_right)
right_btn.grid(column=1, row=1)

change_word_wrong()

window.mainloop()

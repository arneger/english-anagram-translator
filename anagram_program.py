from nltk.corpus import words
from tkinter import *
import random

# Function that takes the user-input and checks if there's english words from
# the nltk words list that got the exact same characters as the input.
def anagram_matcher():
    output_word2.config(state=NORMAL)
    output_word2.delete(0.0, END)
    output_word2.config(state=DISABLED)
    the_anagram = input_word2.get("1.0", "end-1c")
    characters = the_anagram.lower()
    if len(characters.split()) > 1:
        output_word2.config(state=NORMAL)
        output_word2.insert(END, " Type only a single word.")
        output_word2.config(state=DISABLED)
    else:
        try: #A try except. If the code doesn't run it's probably because nltk words is not installed (Check README)
            english_words = words.words()
            for word in english_words:
                if sorted(word) == sorted(characters):
                    output_word2.config(state=NORMAL)
                    output_word2.insert(END, "\n " + word)
                    output_word2.config(state=DISABLED)
                else:
                    pass
        except:
            output_word2.config(state=NORMAL)
            output_word2.insert(END, "Error: Check the README")
            output_word2.config(state=DISABLED)

# Function that generates an anagram from the given user input.
def anagram_generator():
    output_word1.config(state=NORMAL)
    output_word1.delete(0.0, END)
    output_word1.config(state=DISABLED)
    the_word = input_word1.get("1.0", "end-1c")
    if len(the_word.split()) > 1:
        output_word1.config(state=NORMAL)
        output_word1.insert(END, " Type only a single word.")
        output_word1.config(state=DISABLED)
    else:
        anagram_list = list(the_word.lower())
        random.shuffle(anagram_list)
        new_anagram = "".join(anagram_list)
        output_word1.config(state=NORMAL)
        output_word1.insert(END, " " + new_anagram)
        output_word1.config(state=DISABLED)


# The GUI
window = Tk()
canvas = Canvas(height=650, width=800, bg="#0d0d0d")
canvas.pack()
window.title("Anagramify")
window.resizable(False,False)

#Mid-frame 1
mid_frame1 = Frame(window, bg="#1a1a1a", bd=10)
mid_frame1.place(relx=0.5, rely=0.08, relwidth=0.7, relheight=0.3, anchor="n")

input_label = Label (mid_frame1, text="Word", bg="#1a1a1a", fg="white", font="arial 15 bold")
input_label.place(relx=0.12, rely=0.15, relwidth=0.2, relheight=0.2)

input_word1 = Text(mid_frame1, font="none 15 bold", bg="#0d0d0d", fg="white", state=None)
input_word1.place(relx=0.02, rely=0.35, relwidth=0.4, relheight=0.3)

translate_button1 = Button(mid_frame1, text=u"\u2b9e", bg="#1a1a1a", fg="white", font="none 15 bold", command=anagram_generator)
translate_button1.place(relx=0.451, rely=0.35, relwidth=0.1, relheight=0.31)

output_label1 = Label (mid_frame1, text="Anagram", bg="#1a1a1a", fg="white", font="arial 15 bold")
output_label1.place(relx=0.68, rely=0.15, relwidth=0.2, relheight=0.2)

output_word1 = Text(mid_frame1, font="none 12 bold", bg="#0d0d0d", fg="white", state=DISABLED)
output_word1.place(relx=0.58, rely=0.35, relwidth=0.4, relheight=0.3)

#mid-frame 2
mid_frame2 = Frame(window, bg="#1a1a1a", bd=10)
mid_frame2.place(relx=0.5, rely=0.4, relwidth=0.7, relheight=0.52, anchor="n")

input_label2 = Label (mid_frame2, text="Anagram", bg="#1a1a1a", fg="white", font="arial 15 bold")
input_label2.place(relx=0.12, rely=0.23, relwidth=0.2, relheight=0.2)

input_word2 = Text(mid_frame2, font="none 15 bold", bg="#0d0d0d", fg="white")
input_word2.place(relx=0.02, rely=0.4 , relwidth=0.4, relheight=0.17)

translate_button2 = Button(mid_frame2, text=u"\u2b9e", bg="#1a1a1a", fg="white", font="none 15 bold", command=anagram_matcher)
translate_button2.place(relx=0.451, rely=0.4, relwidth=0.1, relheight=0.175)

output_label2 = Label (mid_frame2, text="Anagram Matches", bg="#1a1a1a", fg="white", font="arial 15 bold")
output_label2.place(relx=0.585, rely=0.03, relwidth=0.4, relheight=0.1)

output_word2 = Text(mid_frame2, font="none 12 bold", bg="#0d0d0d", fg="white", state=DISABLED)
output_word2.place(relx=0.58, rely=0.15 , relwidth=0.4, relheight=0.7)

window.mainloop()
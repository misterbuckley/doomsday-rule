#!/usr/bin/python3

import tkinter as tk

from doomsday import get_random_date

START_DATE = "1700-01-01"
END_DATE = "2299-12-31"


class DoomsdayGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Doomsday Practice")

        self.correct = 0
        self.incorrect = 0
        self.random_date = None

        self.date_label = tk.Label(master, font=("Helvetica", 16))
        self.date_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        button_frame = tk.Frame(master)
        button_frame.pack(pady=5)

        self.guess_button = tk.Button(button_frame, text="Guess", width=10,
                                      command=self.check_guess)
        self.guess_button.grid(row=0, column=0, padx=5)

        self.skip_button = tk.Button(button_frame, text="Skip", width=10,
                                     command=self.next_date)
        self.skip_button.grid(row=0, column=1, padx=5)

        self.giveup_button = tk.Button(button_frame, text="Give Up", width=10,
                                       command=self.give_up)
        self.giveup_button.grid(row=0, column=2, padx=5)

        self.message_label = tk.Label(master, font=("Helvetica", 12))
        self.message_label.pack(pady=5)

        self.score_label = tk.Label(master, font=("Helvetica", 12))
        self.score_label.pack(pady=5)

        self.next_date()

    def next_date(self):
        self.random_date = get_random_date(START_DATE, END_DATE)
        date_str = self.random_date.strftime("%B %d, %Y").replace(" 0", " ")
        self.date_label.config(text=date_str)
        self.entry.delete(0, tk.END)
        self.message_label.config(text="")
        self.update_score()
        self.entry.focus_set()

    def check_guess(self):
        guess = self.entry.get().strip()
        if not guess:
            return
        day_of_week = self.random_date.strftime("%A")
        if day_of_week.lower().startswith(guess.lower()):
            self.correct += 1
            self.message_label.config(text="Correct!")
        else:
            self.incorrect += 1
            self.message_label.config(
                text=f"Incorrect! It was a {day_of_week}.")
        self.update_score()
        self.master.after(500, self.next_date)

    def give_up(self):
        day_of_week = self.random_date.strftime("%A")
        self.incorrect += 1
        self.message_label.config(text=f"The correct day was {day_of_week}.")
        self.update_score()
        self.master.after(500, self.next_date)

    def update_score(self):
        self.score_label.config(
            text=f"Correct: {self.correct}    Incorrect: {self.incorrect}")


def main():
    root = tk.Tk()
    DoomsdayGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

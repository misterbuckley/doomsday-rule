#!/usr/bin/python3

import tkinter as tk

from doomsday import get_random_date

START_DATE = "1700-01-01"
END_DATE = "2299-12-31"

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]


def century_anchor(year):
    """Return the anchor weekday for the given year"""
    century = year // 100
    return (5 * (century % 4) + 2) % 7


def year_doomsday(year):
    y = year % 100
    return (century_anchor(year) + y + y // 4) % 7


class DoomsdayGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Doomsday Practice")

        self.correct = 0
        self.incorrect = 0
        self.random_date = None
        self.hint_stage = 0

        self.date_label = tk.Label(master, font=("Helvetica", 16))
        self.date_label.pack(pady=10)

        self.days_frame = tk.Frame(master)
        self.days_frame.pack(pady=5)

        top_row = tk.Frame(self.days_frame)
        top_row.pack(anchor="center")
        bottom_row = tk.Frame(self.days_frame)
        bottom_row.pack(anchor="center")

        self.day_buttons = {}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        for i, day in enumerate(days):
            parent = top_row if i < 4 else bottom_row
            btn = tk.Button(parent, text=day, width=10,
                            command=lambda d=day: self.check_guess(d))
            btn.pack(side=tk.LEFT, padx=3, pady=2)
            self.day_buttons[day] = btn

        control_frame = tk.Frame(master)
        control_frame.pack()

        self.skip_button = tk.Button(control_frame, text="Skip", width=10,
                                     command=self.next_date)
        self.skip_button.pack(side=tk.LEFT, padx=3, pady=5)

        self.giveup_button = tk.Button(control_frame, text="Give Up", width=10,
                                       command=self.give_up)
        self.giveup_button.pack(side=tk.LEFT, padx=3, pady=5)

        self.next_button = tk.Button(master, text="Next", width=10,
                                     command=self.next_date)

        self.message_label = tk.Label(master, font=("Helvetica", 12))
        self.message_label.pack(pady=5)

        self.score_label = tk.Label(master, font=("Helvetica", 12))
        self.score_label.pack(pady=5)

        self.hint_button = tk.Button(master, text="Hint", width=10,
                                     command=self.show_hint)
        self.hint_button.pack(pady=5)

        self.hint_label = tk.Label(master, font=("Helvetica", 12))
        self.hint_label.pack(pady=5)

        self.next_date()

    def next_date(self):
        self.random_date = get_random_date(START_DATE, END_DATE)
        date_str = self.random_date.strftime("%B %d, %Y").replace(" 0", " ")
        self.date_label.config(text=date_str)
        self.message_label.config(text="")
        self.update_score()
        self.hint_label.config(text="")
        self.hint_stage = 0
        self.next_button.pack_forget()
        self.days_frame.pack(pady=5)
        for btn in self.day_buttons.values():
            btn.config(state=tk.NORMAL)
        self.skip_button.config(state=tk.NORMAL)
        self.giveup_button.config(state=tk.NORMAL)

    def check_guess(self, guess):
        day_of_week = self.random_date.strftime("%A")
        for btn in self.day_buttons.values():
            btn.config(state=tk.DISABLED)
        if day_of_week.lower().startswith(guess.lower()):
            self.correct += 1
            self.message_label.config(text="Correct!")
        else:
            self.incorrect += 1
            self.message_label.config(
                text=f"Incorrect! It was a {day_of_week}.")
        self.update_score()
        self.days_frame.pack_forget()
        self.skip_button.config(state=tk.DISABLED)
        self.giveup_button.config(state=tk.DISABLED)
        self.next_button.pack(pady=5)

    def give_up(self):
        day_of_week = self.random_date.strftime("%A")
        self.incorrect += 1
        self.message_label.config(text=f"The correct day was {day_of_week}.")
        self.update_score()
        for btn in self.day_buttons.values():
            btn.config(state=tk.DISABLED)
        self.master.after(500, self.next_date)

    def update_score(self):
        self.score_label.config(
            text=f"Correct: {self.correct}    Incorrect: {self.incorrect}")

    def show_hint(self):
        if self.hint_stage == 0:
            anchor = DAYS[century_anchor(self.random_date.year)]
            century = (self.random_date.year // 100) * 100
            self.hint_label.config(
                text=f"Century doomsday for {century}s: {anchor}")
            self.hint_stage = 1
        elif self.hint_stage == 1:
            dooms = DAYS[year_doomsday(self.random_date.year)]
            self.hint_label.config(
                text=f"Year doomsday for {self.random_date.year}: {dooms}")
            self.hint_stage = 2


def main():
    root = tk.Tk()
    DoomsdayGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

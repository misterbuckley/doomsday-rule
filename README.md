# The Doomsday Rule

This project contains small tools to practice John Conway's Doomsday Rule, an algorithm that lets you determine the day of the week for any given date.

## Command line interface

Run `python doomsday.py` to practice guessing the weekday for random dates in the terminal.

## Graphical interface

 A simple Tkinter GUI is provided in `doomsday_gui.py`. Run `python doomsday_gui.py` and use the weekday buttons to make your guess, or press **Skip** or **Give Up**. After each guess the weekday buttons disappear and a **Next** button lets you move on when ready. The interface keeps a running tally of correct and incorrect answers. A **Hint** button reveals the century's doomsday on the first click and the year's doomsday on the second.

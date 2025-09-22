"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

import tkinter as tk
from tkinter import ttk

class Elements:
    def __init__(self):

def create_window():
    first_numb = "12345"

    main_window = tk.Tk()
    main_window.title("Calculator")
    main_window.geometry("400x400")

    entry_1 = tk.Entry(main_window, width=20)
    entry_1.grid(row=0, column=0, padx=10, pady=4, ipady=4)
    label_1 = tk.Label(main_window, width=20, text=first_numb)
    label_1.grid(row=1, column=0, padx=10, pady=4)

    if __name__ == '__main__':
        main_window.mainloop()


def perform_operation(first_numb, second_numb, operation):
    if operation == "+":
        return first_numb + second_numb
    elif operation == "-":
        return first_numb - second_numb
    elif operation == "*":
        return first_numb * second_numb
    elif operation == "/":
        return first_numb / second_numb
    else:
        return ("Invalid operation")


print(perform_operation(12, 3, "*"))


create_window()


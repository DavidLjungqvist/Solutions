"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

import tkinter as tk
from tkinter import ttk


# class Elements:
#     def __init__(self, main_window):
#         self.entry_1 = tk.Entry(main_window,)





main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry("400x400")






def reset():
    entry_2.delete(0, tk.END)
    entry_1.configure(state='normal')
    entry_1.delete(0, tk.END)
    entry_2.configure(state='readonly')
    label_1.config(text="")


def read_left_entry():
    entry_1.configure(state='readonly')
    entry_2.configure(state='normal')
    return entry_1.get()

def read_right_entry():
    return entry_2.get()



def choose_operator_add():
    current_calculation = label_1.cget("text")
    num_1 = read_left_entry()
    current_calculation = num_1
    label_1.config(text=str(current_calculation) + "+")


# def choose_operator_subtract():
#     populate_left_entry()
#     label_1.config(text=f"{first_numb} -")
#
#
# def choose_operator_divide():
#     populate_left_entry()
#     label_1.config(text=f"{first_numb} /")
#
#
# def choose_operator_multiply():
#     populate_left_entry()
#     label_1.config(text=current_string)
#
#
def calculate_result_add():


    result = float(read_left_entry()) + float(read_right_entry())
    entry_1.configure(state='normal')
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_1.insert(0, result)
    entry_1.configure(state='readonly')


label_1 = tk.Label(main_window, width=20, text="")
label_1.grid(row=0, column=0, padx=10, pady=4)
entry_1 = tk.Entry(main_window, width=20)
entry_1.grid(row=1, column=0, padx=10, pady=4, ipady=4)
entry_2 = tk.Entry(main_window, width=20, state="readonly")
entry_2.grid(row=1, column=1, padx=10, pady=4, ipady=4)
button_1 = tk.Button(main_window, text="+", command=choose_operator_add)
button_1.grid(row=2, column=0, padx=10, pady=4,)
# button_2 = tk.Button(main_window, text="-", command=choose_operator_subtract)
# button_2.grid(row=2, column=1, padx=10, pady=4,)
# button_3 = tk.Button(main_window, text="/", command=choose_operator_divide)
# button_3.grid(row=3, column=0, padx=10, pady=4,)
# button_4 = tk.Button(main_window, text="*", command=choose_operator_multiply)
# button_4.grid(row=3, column=1, padx=10, pady=4,)
button_5 = tk.Button(main_window, text="=", command=calculate_result_add)
button_5.grid(row=2, column=1, padx=10, pady=4,)
button_6 = tk.Button(main_window, text="=", command=reset)
button_6.grid(row=3, column=0, padx=10, pady=4,)


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


if __name__ == '__main__':
    main_window.mainloop()
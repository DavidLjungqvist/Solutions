""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title("My First GUI")
main_window.geometry("450x200")


pady = 4
padx = 8


def clear_entry_boxes():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)


frame_1 = tk.LabelFrame(main_window, text="Container", width=400, height=140)
frame_1.grid(row=0, column=0, padx= 10, pady=10)

frame_1.grid_propagate(False)

frame_1.grid_rowconfigure(0, weight= 1)
frame_1.grid_rowconfigure(2, weight= 1)
frame_1.grid_columnconfigure(0, weight= 1)
frame_1.grid_columnconfigure(2, weight= 1)

frame_2 = tk.Frame(frame_1)
frame_2.grid(row=0, column=0)

frame_3 = tk.Frame(frame_1)
frame_3.grid(row=1, column=0)


label_1 = tk.Label(frame_2, text="Id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)
label_2 = tk.Label(frame_2, text="Weight")
label_2.grid(row=0, column=1, padx=padx, pady=pady)
label_3 = tk.Label(frame_2, text="Destination")
label_3.grid(row=0, column=2, padx=padx, pady=pady)
label_4 = tk.Label(frame_2, text="Weather")
label_4.grid(row=0, column=3, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_2, width=4)
entry_1.grid(row=1, column=0, padx=padx, pady=pady)
entry_2 = tk.Entry(frame_2, width=9)
entry_2.grid(row=1, column=1, padx=padx, pady=pady)
entry_3 = tk.Entry(frame_2, width=20)
entry_3.grid(row=1, column=2, padx=padx, pady=pady)
entry_4 = tk.Entry(frame_2, width=16)
entry_4.grid(row=1, column=3, padx=padx, pady=pady)

button_1 = tk.Button(frame_3, text="Create")
button_1.grid(row=2, column=0, padx=padx, pady=pady)
button_2 = tk.Button(frame_3, text="Update")
button_2.grid(row=2, column=1, padx=padx, pady=pady)
button_3 = tk.Button(frame_3, text="Delete")
button_3.grid(row=2, column=2, padx=padx, pady=pady)
button_4 = tk.Button(frame_3, text="Clear Entry Boxes", command=clear_entry_boxes)
button_4.grid(row=2, column=3, padx=padx, pady=pady)

if __name__ == '__main__':
    main_window.mainloop()
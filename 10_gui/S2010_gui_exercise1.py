"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title("My First GUI")
main_window.geometry("250x300")


pady = 4
padx = 4


frame_1 = tk.LabelFrame(main_window, text="Container", width=100, height=140)
frame_1.grid(row=0, column=0, padx= 10, pady=10)

frame_1.grid_propagate(False)

frame_1.grid_rowconfigure(0, weight= 1)
frame_1.grid_rowconfigure(2, weight= 1)
frame_1.grid_columnconfigure(0, weight= 1)
frame_1.grid_columnconfigure(2, weight= 1)

label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=0, column=1, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=4)
entry_1.grid(row=1, column=1, padx=padx, pady=pady)

button_1 = tk.Button(frame_1, text="Create")
button_1.grid(row=2, column=1, padx=padx, pady=pady)

if __name__ == '__main__':
    main_window.mainloop()
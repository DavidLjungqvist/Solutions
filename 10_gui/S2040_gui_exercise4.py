""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


import tkinter as tk
from tkinter import ttk


main_window = tk.Tk()
main_window.title("My First GUI")
main_window.geometry("600x800")


pady = 4
padx = 8

rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#773333"  # color of selected row in treeview

evenrow = "#ddeedd"
oddrow = "#cce0cc"


test_data_list = []
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))




def clear_entry_boxes():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)


def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_1.insert(0, values[0])
    entry_2.insert(0, values[1])
    entry_3.insert(0, values[2])


def read_table(tree):  # fill tree with test data
    count = 0
    for record in test_data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1


frame_1 = tk.LabelFrame(main_window, text="Container", width=400, height=400)
frame_1.grid(row=0, column=0, padx= 10, pady=10)

frame_1.grid_propagate(False)

frame_1.grid_rowconfigure(0, weight= 1)
frame_1.grid_rowconfigure(2, weight= 1)
frame_1.grid_columnconfigure(0, weight= 1)
frame_1.grid_columnconfigure(2, weight= 1)


frame_2 = tk.Frame(frame_1, height=400)
frame_2.grid(row=0, column=0, padx=padx)

frame_3 = tk.Frame(frame_1)
frame_3.grid(row=1, column=0, padx=padx)

frame_4 = tk.Frame(frame_1)
frame_4.grid(row=2, column=0, padx=padx)


tree_1_scrollbar = tk.Scrollbar(frame_2)
tree_1_scrollbar.grid(row=0, column=1, sticky='ns')
tree_1 = ttk.Treeview(frame_2, yscrollcommand=tree_1_scrollbar.set, height=10)
tree_1.grid(row=0, column=0)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")

tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=60)
tree_1.column("col2", anchor=tk.W, width=90)
tree_1.column("col3", anchor=tk.W, width=200)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="ID", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)




style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview


tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)


label_1 = tk.Label(frame_3, text="Id")
label_1.grid(row=0, column=0, padx=padx, pady=pady)
label_2 = tk.Label(frame_3, text="Weight")
label_2.grid(row=0, column=1, padx=padx, pady=pady)
label_3 = tk.Label(frame_3, text="Destination")
label_3.grid(row=0, column=2, padx=padx, pady=pady)
label_4 = tk.Label(frame_3, text="Weather")
label_4.grid(row=0, column=3, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_3, width=4)
entry_1.grid(row=1, column=0, padx=padx, pady=pady)
entry_2 = tk.Entry(frame_3, width=9)
entry_2.grid(row=1, column=1, padx=padx, pady=pady)
entry_3 = tk.Entry(frame_3, width=20)
entry_3.grid(row=1, column=2, padx=padx, pady=pady)
entry_4 = tk.Entry(frame_3, width=16)
entry_4.grid(row=1, column=3, padx=padx, pady=pady)

button_1 = tk.Button(frame_4, text="Create")
button_1.grid(row=2, column=0, padx=padx, pady=pady)
button_2 = tk.Button(frame_4, text="Update")
button_2.grid(row=2, column=1, padx=padx, pady=pady)
button_3 = tk.Button(frame_4, text="Delete")
button_3.grid(row=2, column=2, padx=padx, pady=pady)
button_4 = tk.Button(frame_4, text="Clear Entry Boxes", command=clear_entry_boxes)
button_4.grid(row=2, column=3, padx=padx, pady=pady)


tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event,tree_1))

read_table(tree_1)


if __name__ == '__main__':
    main_window.mainloop()
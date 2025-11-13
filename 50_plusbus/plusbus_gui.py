import tkinter
import tkinter as tk
from tkinter import ttk

from sqlalchemy import values
from sqlalchemy.dialects.mssql.information_schema import columns

import plusbus_data as pbd
import plusbus_sql as pbsql

padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"


def read_customer_entries():
    return entry_customer_id.get(), entry_customer_surname.get(), entry_customer_contact.get(),

def clear_customer_entries():
    entry_customer_id.delete(0, tk.END)
    entry_customer_surname.delete(0, tk.END)
    entry_customer_contact.delete(0, tk.END)

def write_customer_entries(values):
    entry_customer_id.insert(0, values[0])
    entry_customer_surname.insert(0, values[1])
    entry_customer_contact.insert(0, values[2])

def edit_customer(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_customer_entries()
    write_customer_entries(values)

def create_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.create_record(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)

def update_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.update_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)

def delete_customer(tree, record):
    customer = pbd.Customer.convert_from_tuple(record)
    pbsql.delete_soft_customer(customer)
    clear_customer_entries()
    refresh_treeview(tree, pbd.Customer)


def read_table(tree, class_):
    count = 0
    result = pbsql.select_all(class_)
    for record in result:
        if record.valid():
            if count % 2 == 0:
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))
            else:
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))
            count += 1

def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)

def empty_treeview(tree):
    tree.delete(*tree.get_children())


main_window = tk.Tk()
main_window.title('Plusbus Opgave')
main_window.geometry("1000x500")

style = ttk.Style()
style.theme_use('default')

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

frame_customer = tk.LabelFrame(main_window, text="Kunder")
frame_customer.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_customer = ttk.Frame(frame_customer)
tree_frame_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer = ttk.Scrollbar(tree_frame_customer)
tree_scroll_customer.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_customer = ttk.Treeview(tree_frame_customer, yscrollcommand=tree_scroll_customer.set, selectmode="browse")
tree_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer.config(command=tree_customer.yview)

tree_customer['columns'] = ("id", "surname", "contact_info")
tree_customer.column("#0", width=0, stretch=tk.NO)
tree_customer.column("id", anchor=tk.E, width=60)
tree_customer.column("surname", anchor=tk.CENTER, width=140)
tree_customer.column("contact_info", anchor=tk.W, width=200)
tree_customer.heading("#0", text="", anchor=tk.W)
tree_customer.heading("id", text="Kunde ID", anchor=tk.CENTER)
tree_customer.heading("surname", text="Efternavn", anchor=tk.CENTER)
tree_customer.heading("contact_info", text="Kontakt Information", anchor=tk.CENTER)
tree_customer.tag_configure('oddrow', background=oddrow)
tree_customer.tag_configure('evenrow', background=evenrow)
tree_customer.bind("<ButtonRelease-1>", lambda event: edit_customer(event, tree_customer))

controls_frame_customer = tk.Frame(frame_customer)
controls_frame_customer.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_customer = tk.Frame(controls_frame_customer)
edit_frame_customer.grid(row=0, column=0, padx=padx, pady=pady)

label_customer_id = tk.Label(edit_frame_customer, text="ID")
label_customer_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_customer_id = tk.Entry(edit_frame_customer, width=4, justify="right")
entry_customer_id.grid(row=1, column=0, padx=padx, pady=pady)

label_customer_surname = tk.Label(edit_frame_customer, text="Efternavn")
label_customer_surname.grid(row=0, column=1, padx=padx, pady=pady)
entry_customer_surname = tk.Entry(edit_frame_customer, width=20)
entry_customer_surname.grid(row=1, column=1, padx=padx, pady=pady)

label_customer_contact = tk.Label(edit_frame_customer, text="Kontakt Information")
label_customer_contact.grid(row=0, column=2, padx=padx, pady=pady)
entry_customer_contact = tk.Entry(edit_frame_customer, width=24)
entry_customer_contact.grid(row=1, column=2, padx=padx, pady=pady)

button_frame_customer = tk.Frame(controls_frame_customer)
button_frame_customer.grid(row=1, column=0, padx=padx, pady=pady)

button_create_customer = tk.Button(button_frame_customer, text="Opret Ny", command=lambda: create_customer(tree_customer, read_customer_entries()))
button_create_customer.grid(row=0, column=0, padx=padx, pady=pady)
button_update_customer = tk.Button(button_frame_customer, text="Opdater", command=lambda: update_customer(tree_customer, read_customer_entries()))
button_update_customer.grid(row=0, column=1, padx=padx, pady=pady)
button_delete_customer = tk.Button(button_frame_customer, text="Slet", command=lambda: delete_customer(tree_customer, read_customer_entries()))
button_delete_customer.grid(row=0, column=2, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_customer, text="Ryd Felter", command=clear_customer_entries)
button_clear_boxes.grid(row=0, column=3, padx=padx, pady=pady)

frame_travel = tk.LabelFrame(main_window, text="Rejser")
frame_travel.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

tree_frame_travel = tk.Frame(frame_travel)
tree_frame_travel.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_routes = tk.Scrollbar(frame_travel)
tree_scroll_routes.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_travel = ttk.Treeview(tree_frame_travel, yscrollcommand=tree_scroll_routes.set, selectmode="browse")
tree_travel.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_routes.config(command=tree_travel.yview)

tree_travel['columns'] = ("id", "route", "date", "capacity")
tree_travel.column("#0", width=0, stretch=tk.NO)
tree_travel.column("id", anchor=tk.E, width=40)
tree_travel.column("route", anchor=tk.E, width=100)
tree_travel.column("date", anchor=tk.E, width=100)
tree_travel.column("capacity", anchor=tk.E, width=100)
tree_travel.heading("#0", text="", anchor=tk.W)
tree_travel.heading("id", text="ID", anchor=tk.CENTER)
tree_travel.heading("route", text="Rute", anchor=tk.CENTER)
tree_travel.heading("date", text="Dato", anchor=tk.CENTER)
tree_travel.heading("capacity", text="Pladser", anchor=tk.CENTER)
tree_travel.tag_configure('oddrow', background=oddrow)
tree_travel.tag_configure('evenrow', background=evenrow)

# tree_travel.bind("<ButtonRelease1>", lambda event: edit_routes(event, tree_travel))


controls_frame_travel = tk.Frame(frame_travel)
controls_frame_travel.grid(row=1, column=0, padx=padx, pady=pady)

edit_frame_travel = tk.Frame(controls_frame_travel)
edit_frame_travel.grid(row=0, column=0, padx=padx, pady=pady)

label_travel_id = tk.Label(edit_frame_travel, text="ID")
label_travel_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_travel_id = tk.Entry(edit_frame_travel, width=4, justify="right")
entry_travel_id.grid(row=1, column=0, padx=padx, pady=pady)

label_travel_date = tk.Label(edit_frame_travel, text="Dato")
label_travel_date.grid(row=0, column=1, padx=padx, pady=pady)
entry_travel_date = tk.Entry(edit_frame_travel, width=12, justify="right")
entry_travel_date.grid(row=1, column=1, padx=padx, pady=pady)

label_travel_capacity = tk.Label(edit_frame_travel, text="Pladser")
label_travel_capacity.grid(row=0, column=2, padx=padx, pady=pady)
entry_travel_capacity = tk.Entry(edit_frame_travel, width=4, justify="right")
entry_travel_capacity.grid(row=1, column=2, padx=padx, pady=pady)

label_travel_route_route = tk.Label(edit_frame_travel, text="Rute")
label_travel_route_route.grid(row=0, column=3, padx=padx, pady=pady)
entry_travel_route_route = tk.Entry(edit_frame_travel, width=24, justify="right")
entry_travel_route_route.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_travel = tk.Label(controls_frame_travel)
button_frame_travel.grid(row=1, column=0, padx=padx, pady=pady)

button_create_travel = tk.Button(button_frame_travel, text="Opret Ny", command=lambda: create_travel(tree_customer, read_travel_entries()))
button_create_travel.grid(row=0, column=0, padx=padx, pady=pady)
button_update_travel = tk.Button(button_frame_travel, text="Opdater", command=lambda: update_travel(tree_customer, read_travel_entries()))
button_update_travel.grid(row=0, column=1, padx=padx, pady=pady)
button_delete_travel = tk.Button(button_frame_travel, text="Slet", command=lambda: delete_travel(tree_customer, read_travel_entries()))
button_delete_travel.grid(row=0, column=2, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_travel, text="Ryd Felter", command=clear_travel_entries)
button_clear_boxes.grid(row=0, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    refresh_treeview(tree_customer, pbd.Customer)
    main_window.mainloop()

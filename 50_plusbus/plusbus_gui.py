import tkinter
import tkinter as tk
from tkinter import ttk
import plusbus_data as pbd
import plusbus_sql as pbsql
import plusbus_func as pbf

padx = 8
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"
oddrow = "#dddddd"
evenrow = "#cccccc"

#  region customer functions
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
#  endregion customer functions
#  region travel functions
def read_travel_entries():
    return entry_travel_id.get(), entry_travel_route.get(), entry_travel_date.get(), entry_travel_capacity.get(),

def clear_travel_entries():
    entry_travel_id.delete(0, tk.END)
    entry_travel_route.delete(0, tk.END)
    entry_travel_date.delete(0, tk.END)
    entry_travel_capacity.delete(0, tk.END)

def write_travel_entries(values):
    entry_travel_id.insert(0, values[0])
    entry_travel_route.insert(0, values[1])
    entry_travel_date.insert(0, values[2])
    entry_travel_capacity.insert(0, values[3])

def edit_travel(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_travel_entries()
    write_travel_entries(values)

def create_travel(tree, record):
    travel = pbd.Travel.convert_from_tuple(record)
    pbsql.create_record(travel)
    clear_travel_entries()
    refresh_treeview(tree, pbd.Travel)

def update_travel(tree, record):
    travel = pbd.Travel.convert_from_tuple(record)
    pbsql.update_travel(travel)
    clear_travel_entries()
    refresh_treeview(tree, pbd.Travel)

def delete_travel(tree, record):
    travel = pbd.Travel.convert_from_tuple(record)
    pbsql.delete_soft_travel(travel)
    clear_travel_entries()
    refresh_treeview(tree, pbd.Travel)
#  endregion travel functions
#  region booking functions
def read_booking_entries():
    return entry_booking_booking_id.get(), entry_booking_customer_id.get(), entry_booking_travel_id.get(), entry_booking_reserved_seats.get(),

def clear_booking_entries():
    entry_booking_booking_id.delete(0, tk.END)
    entry_booking_customer_id.delete(0, tk.END)
    entry_booking_travel_id.delete(0, tk.END)
    entry_booking_reserved_seats.delete(0, tk.END)

def write_booking_entries(values):
    entry_booking_booking_id.insert(0, values[0])
    entry_booking_customer_id.insert(0, values[1])
    entry_booking_travel_id.insert(0, values[2])
    entry_booking_reserved_seats.insert(0, values[3])

def edit_booking(_, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    clear_booking_entries()
    write_booking_entries(values)

def create_booking(tree, record):
    booking = pbd.Booking.convert_from_tuple(record)
    capacity_available = pbf.capacity_available(booking, pbsql.get_record(pbd.Travel, booking.travel_id))
    if capacity_available:
        pbsql.create_record(booking)
        clear_booking_entries()
        refresh_treeview(tree, pbd.Booking)
    else:
        print("not enough space available")

def update_booking(tree, record):  # Will be wrong if you try to update because it will try to count reserved spots of itself on the datebase
    booking = pbd.Booking.convert_from_tuple(record)
    capacity_available = pbf.capacity_available(booking, pbsql.get_record(pbd.Travel, booking.travel_id))
    if capacity_available:
        pbsql.update_booking(booking)
        clear_booking_entries()
        refresh_treeview(tree, pbd.Booking)
    else:
        print("not enough space available")

def delete_booking(tree, record):
    booking = pbd.Booking.convert_from_tuple(record)
    pbsql.delete_hard_booking(booking)
    clear_booking_entries()
    refresh_treeview(tree, pbd.Booking)

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


#hardcode 1st line in Bookinger

# exit(123)


#  region common widgets
main_window = tk.Tk()
main_window.title('Plusbus Opgave')
main_window.geometry("1400x500")

style = ttk.Style()
style.theme_use('default')

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])
#  endregion common widgets

#  region customer widgets
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
#  endregion customer widgets
#  region travel widgets
frame_travel = tk.LabelFrame(main_window, text="Rejser")
frame_travel.grid(row=0, column=1, padx=padx, pady=pady, sticky=tk.N)

tree_frame_travel = tk.Frame(frame_travel)
tree_frame_travel.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_routes = tk.Scrollbar(frame_travel)
tree_scroll_routes.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_travel = ttk.Treeview(tree_frame_travel, yscrollcommand=tree_scroll_routes.set, selectmode="browse")
tree_travel.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_routes.config(command=tree_travel.yview)

tree_travel['columns'] = ("id", "route", "date", "capacity")
tree_travel.column("#0", width=0, stretch=tk.NO)
tree_travel.column("id", anchor=tk.E, width=50)
tree_travel.column("route", anchor=tk.E, width=220)
tree_travel.column("date", anchor=tk.E, width=80)
tree_travel.column("capacity", anchor=tk.E, width=50)
tree_travel.heading("#0", text="", anchor=tk.W)
tree_travel.heading("id", text="ID", anchor=tk.CENTER)
tree_travel.heading("route", text="Rute", anchor=tk.CENTER)
tree_travel.heading("date", text="Dato", anchor=tk.CENTER)
tree_travel.heading("capacity", text="Pladser", anchor=tk.CENTER)
tree_travel.tag_configure('oddrow', background=oddrow)
tree_travel.tag_configure('evenrow', background=evenrow)
tree_travel.bind("<ButtonRelease-1>", lambda event: edit_travel(event, tree_travel))


controls_frame_travel = tk.Frame(frame_travel)
controls_frame_travel.grid(row=1, column=0, padx=padx, pady=pady)

edit_frame_travel = tk.Frame(controls_frame_travel)
edit_frame_travel.grid(row=0, column=0, padx=padx, pady=pady)

label_travel_id = tk.Label(edit_frame_travel, text="ID")
label_travel_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_travel_id = tk.Entry(edit_frame_travel, width=6, justify="right")
entry_travel_id.grid(row=1, column=0, padx=padx, pady=pady)

label_travel_route = tk.Label(edit_frame_travel, text="Rute")
label_travel_route.grid(row=0, column=1, padx=padx, pady=pady)
entry_travel_route = tk.Entry(edit_frame_travel, width=24, justify="right")
entry_travel_route.grid(row=1, column=1, padx=padx, pady=pady)

label_travel_date = tk.Label(edit_frame_travel, text="Dato")
label_travel_date.grid(row=0, column=2, padx=padx, pady=pady)
entry_travel_date = tk.Entry(edit_frame_travel, width=12, justify="right")
entry_travel_date.grid(row=1, column=2, padx=padx, pady=pady)

label_travel_capacity = tk.Label(edit_frame_travel, text="Pladser")
label_travel_capacity.grid(row=0, column=3, padx=padx, pady=pady)
entry_travel_capacity = tk.Entry(edit_frame_travel, width=4, justify="right")
entry_travel_capacity.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_travel = tk.Label(controls_frame_travel)
button_frame_travel.grid(row=1, column=0, padx=padx, pady=pady)

button_create_travel = tk.Button(button_frame_travel, text="Opret Ny", command=lambda: create_travel(tree_travel, read_travel_entries()))
button_create_travel.grid(row=0, column=0, padx=padx, pady=pady)
button_update_travel = tk.Button(button_frame_travel, text="Opdater", command=lambda: update_travel(tree_travel, read_travel_entries()))
button_update_travel.grid(row=0, column=1, padx=padx, pady=pady)
button_delete_travel = tk.Button(button_frame_travel, text="Slet", command=lambda : delete_travel(tree_travel, read_travel_entries()))
button_delete_travel.grid(row=0, column=2, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_travel, text="Ryd Felter", command=clear_travel_entries)
button_clear_boxes.grid(row=0, column=3, padx=padx, pady=pady)
#  endregion travel widgets
#  region booking widgets
frame_booking = tk.LabelFrame(main_window, text="Bookinger")
frame_booking.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

tree_frame_booking = tk.Frame(frame_booking)
tree_frame_booking.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_booking = tk.Scrollbar(frame_booking)
tree_scroll_booking.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_booking = ttk.Treeview(tree_frame_booking, yscrollcommand=tree_scroll_booking.set, selectmode="browse")
tree_booking.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_booking.config(command=tree_booking.yview)

tree_booking['column'] = ("id", "customer_id", "travel_id", "reserved_seats")
tree_booking.column("#0", width=0, stretch=tk.NO)
tree_booking.column("id", anchor=tk.E, width=90)
tree_booking.column("customer_id", anchor=tk.E, width=90)
tree_booking.column("travel_id", anchor=tk.E, width=90)
tree_booking.column("reserved_seats", anchor=tk.E, width=110)
tree_booking.heading("#0", text="", anchor=tk.W)
tree_booking.heading("id", text="Booking ID", anchor=tk.CENTER)
tree_booking.heading("customer_id", text="Kunde ID", anchor=tk.CENTER)
tree_booking.heading("travel_id", text="Rejse ID", anchor=tk.CENTER)
tree_booking.heading("reserved_seats", text="Reserveret pladser", anchor=tk.CENTER)
tree_booking.tag_configure('oddrow', background=oddrow)
tree_booking.tag_configure('evenrow', background=evenrow)
tree_booking.bind("<ButtonRelease-1>", lambda event: edit_booking(event, tree_booking))

controls_frame_booking = tk.Frame(frame_booking)
controls_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)

edit_frame_booking = tk.Frame(controls_frame_booking)
edit_frame_booking.grid(row=0, column=0, padx=padx, pady=pady)

label_booking_booking_id = tk.Label(edit_frame_booking, text="Booking ID")
label_booking_booking_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_booking_booking_id = tk.Entry(edit_frame_booking, width=6, justify="right")
entry_booking_booking_id.grid(row=1, column=0, padx=padx, pady=pady)

label_booking_customer_id = tk.Label(edit_frame_booking, text="Kunde ID")
label_booking_customer_id.grid(row=0, column=1, padx=padx, pady=pady)
entry_booking_customer_id = tk.Entry(edit_frame_booking, width=6, justify="right")
entry_booking_customer_id.grid(row=1, column=1, padx=padx, pady=pady)

label_booking_travel_id = tk.Label(edit_frame_booking, text="Rejse ID")
label_booking_travel_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_booking_travel_id = tk.Entry(edit_frame_booking, width=6, justify="right")
entry_booking_travel_id.grid(row=1, column=2, padx=padx, pady=pady)

label_booking_reserved_seats = tk.Label(edit_frame_booking, text="Reserveret pladser")
label_booking_reserved_seats.grid(row=0, column=3, padx=padx, pady=pady)
entry_booking_reserved_seats = tk.Entry(edit_frame_booking, width=6, justify="right")
entry_booking_reserved_seats.grid(row=1, column=3, padx=padx, pady=pady)

button_frame_booking = tk.Frame(controls_frame_booking)
button_frame_booking.grid(row=1, column=0, padx=padx, pady=pady)


button_create_booking = tk.Button(button_frame_booking, text="Opret Ny", command=lambda: create_booking(tree_booking, read_booking_entries()))
button_create_booking.grid(row=0, column=0, padx=padx, pady=pady)
button_update_booking = tk.Button(button_frame_booking, text="Opdater", command=lambda: update_booking(tree_booking, read_booking_entries()))
button_update_booking.grid(row=0, column=1, padx=padx, pady=pady)
button_delete_booking = tk.Button(button_frame_booking, text="Slet", command=lambda: delete_booking(tree_booking, read_booking_entries()))
button_delete_booking.grid(row=0, column=2, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_booking, text="Ryd Felter", command=clear_booking_entries)
button_clear_boxes.grid(row=0, column=3, padx=padx, pady=pady)


if __name__ == "__main__":
    refresh_treeview(tree_customer, pbd.Customer)
    refresh_treeview(tree_travel, pbd.Travel)
    refresh_treeview(tree_booking, pbd.Booking)
    main_window.mainloop()

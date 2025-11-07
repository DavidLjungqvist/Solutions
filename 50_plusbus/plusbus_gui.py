import tkinter as tk
from tkinter import ttk
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

main_window = tk.Tk()
main_window.title('Plusbus Opgave')
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use('default')

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

frame_customer = tk.LabelFrame(main_window, text="Kunder")
frame_customer.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_customer = ttk.Frame(frame_customer)
tree_frame_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer = ttk.Scrollbar(tree_frame_customer)
tree_scroll_customer.grid(row=0, column=1, padx=0, pady= pady, sticky='ns')
tree_customer = ttk.Treeview(tree_frame_customer, yscrollcommand=tree_scroll_customer.set, selectmode="browse")
tree_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer.config(command=tree_customer.yview)

tree_customer['columns'] =("id", "surname", "contact_info")
tree_customer.column("#0", width=0, stretch=tk.NO)
tree_customer.column("id", anchor=tk.E, width=60)
tree_customer.column("surname", anchor=tk.W, width=140)
tree_customer.column("contact_info", anchor=tk.W, width=200)
tree_customer.heading("#0", text="", anchor=tk.W)
tree_customer.heading("id", text="Kunde ID", anchor=tk.CENTER)
tree_customer.heading("surname", text="Efternavn", anchor=tk.CENTER)
tree_customer.heading("contact_info", text="Kontakt Information", anchor=tk.CENTER)
tree_customer.tag_configure('oddrow', background=oddrow)
tree_customer.tag_configure('evenrow', background=evenrow)
# tree_customer.bind()

controls_frame_customer = tk.Frame(frame_customer)
controls_frame_customer.grid(row=3, column=0, padx=padx, pady=pady)



if __name__ == "__main__":
    # refresh_treeview(tree_customer, pbd.Customer)
    main_window.mainloop()
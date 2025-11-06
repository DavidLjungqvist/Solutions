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
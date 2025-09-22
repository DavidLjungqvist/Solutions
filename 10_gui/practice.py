import tkinter
from tkinter import *
from tkinter import messagebox

# top = Tk()
# top.geometry("100x100")
#
# def hello_call_back():
#    msg=messagebox.showinfo( "Hello Python", "Hello World")
# B = Button(top, text ="Hello", command = hello_call_back)
# B.place(x=50,y=50)
# top.mainloop()

root = Tk()
root.title("Simple App")
root.geometry("500x500")

def add_to_list(event=None):
   text = entry.get()
   if text:
      text_list.insert(tkinter.END, text)
      entry.delete(0, tkinter.END)


frame = tkinter.Frame(root)
frame.grid(row=0, column=0)


entry = tkinter.Entry(frame)
entry.grid(row=0, column=0)


entry.bind("<Return>", add_to_list)


entry_button = tkinter.Button(frame, text="Add", command=add_to_list)
entry_button.grid(row=0, column=1,)


text_list = tkinter.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="ew")

root.mainloop()
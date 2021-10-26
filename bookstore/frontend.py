import tkinter as tk
from tkinter.constants import END
from typing import Any
import backend


def delete_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def selected_row(event):
    try:
        global select_tuple
        ind = listbox.curselection()[0]
        select_tuple = listbox.get(ind)
        delete_entries()
        e1.insert(END, select_tuple[1])
        e2.insert(END, select_tuple[2])
        e3.insert(END, select_tuple[3])
        e4.insert(END, select_tuple[4])
        return select_tuple
    except IndexError:
        pass


def view_at():
    listbox.delete(first=0, last=END)
    for item in backend.view():
        listbox.insert(END, item)


def search_entry():
    listbox.delete(first=0, last=END)
    for item in backend.search(title=e_val1.get(), author=e_val2.get(), year=e_val3.get(), isbn=e_val4.get()):
        listbox.insert(END, item)


def add_entry():
    if(e_val1.get() and e_val2.get() and e_val3.get() and e_val4.get()):
        backend.insert(e_val1.get(), e_val2.get(), e_val3.get(), e_val4.get())
        view_at()


def update():
    backend.update(select_tuple[0], e_val1.get(
    ), e_val2.get(), e_val3.get(), e_val4.get())
    view_at()


def delete():
    backend.delete(selected_row(event=Any)[0])
    delete_entries()
    view_at()


def close():
    Bookstore.destroy()


Bookstore = tk.Tk()
Bookstore.wm_title("BookStore")
ls = ["Title", "Author", "Year", "ISBN"]
for index, item in enumerate(ls):
    l1 = tk.Label(Bookstore, text=item)
    l1.grid(row=0 if index < 2 else 1, column=index *
            2 if index < 2 else index*2-4)

e_val1 = tk.StringVar()
e1 = tk.Entry(Bookstore, textvariable=e_val1)
e1.grid(row=0, column=1)
e_val2 = tk.StringVar()
e2 = tk.Entry(Bookstore, textvariable=e_val2)
e2.grid(row=0, column=3)
e_val3 = tk.StringVar()
e3 = tk.Entry(Bookstore, textvariable=e_val3)
e3.grid(row=1, column=1)
e_val4 = tk.StringVar()
e4 = tk.Entry(Bookstore, textvariable=e_val4)
e4.grid(row=1, column=3)


btn_ls = {"View at": view_at, "Search Entry": search_entry, "Add Entry": add_entry,
          "Update": update, "Delete": delete, "Close": close}

listbox = tk.Listbox(Bookstore, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=7, columnspan=2)

sb = tk.Scrollbar(Bookstore)
sb.grid(row=2, rowspan=7, column=2)

listbox.configure(yscrollcommand=sb.set(5, 6))
sb.configure(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", selected_row)

for index, item in enumerate(btn_ls):
    b = tk.Button(Bookstore, text=item, width=12, command=btn_ls[item])
    b.grid(row=index+2, column=3)

Bookstore.mainloop()

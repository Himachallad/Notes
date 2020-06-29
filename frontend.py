from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()
        selected_tuple=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])

        e5.delete(0, END)
        e5.insert(END, selected_tuple[4])
    except Exception as ex:
        pass
def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(name_text.get(), type_text.get(), interest_text.get(), start_text.get(), end_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(name_text.get(), type_text.get(), float(interest_text.get()), start_text.get(), end_text.get())
    list1.delete(0, END)
    view_command()

def delete_command():
    database.delete(selected_tuple[0])  
    view_command()     

def update_command():
    database.update(selected_tuple[0], name_text.get(), type_text.get(), float(interest_text.get()), start_text.get(), end_text.get())
    view_command()

window = Tk()

window.wm_title("Investment Notes")

l1=Label(window, text="Name")
l1.grid(row=0, column=0, pady=5)

l2=Label(window, text="Type")
l2.grid(row=0, column=2, pady=5)

l3=Label(window, text="Interest")
l3.grid(row=1, column=0, pady=5)

l4=Label(window, text="Start date")
l4.grid(row=1, column=2, pady=5)

l5=Label(window, text="End date")
l5.grid(row=2, column=0, pady=5)

name_text=StringVar()
e1=Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

type_text=StringVar()
e2=Entry(window, textvariable=type_text)
e2.grid(row=0, column=3)

interest_text=StringVar()
e3=Entry(window, textvariable=interest_text)
e3.grid(row=1, column=1)

start_text=StringVar()
e4=Entry(window, textvariable=start_text)
e4.grid(row=1, column=3, padx=10)

end_text=StringVar()
e5=Entry(window, textvariable=end_text)
e5.grid(row=2, column=1)


list1 = Listbox(window, height=10, width=40)
list1.grid(row=3, column=0, rowspan=10, columnspan=2, padx=40)

sb1=Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3, column=3, pady=5)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=4, column=3, pady=5)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=5, column=3, pady=5)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=6, column=3, pady=5)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=7, column=3, pady=5)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=3, pady=5)


window.mainloop()
from mongoConnector import connector
from tkinter import *

root = Tk()
root.title('Phone Book')

def save(entries):
    data={'name': entries[0].get(), 'phone': entries[1].get(), 'email': entries[2].get(), 'dob': entries[3].get()}
    print(data)
    connector.saveContact(data)

def newWindow():
    new_window = Toplevel(root)
    new_window.title('Add New Contacts')
    label = Label(new_window, text='New Contact', font=('times new roman', 14))
    name = Label(new_window, text='Name', font=('times new roman', 12))
    phone = Label(new_window, text='Phone', font=('times new roman', 12))
    newphone = Button(new_window, text='+')
    email = Label(new_window, text='Email', font=('times new roman', 12))
    newemail = Button(new_window, text='+')
    dob = Label(new_window, text='DoB', font=('times new roman', 12))
    entries = [
        Entry(new_window, width=30),
        Entry(new_window, width=30),
        Entry(new_window, width=30),
        Entry(new_window, width=30)]
    label.grid(row=0, column=0, columnspan=2)
    name.grid(row=1, column=0)
    phone.grid(row=2, column=0)
    newphone.grid(row=2, column=2)
    email.grid(row=3, column=0)
    newemail.grid(row=3, column=2)
    dob.grid(row=4, column=0)
    entries[0].grid(row=1, column=1)
    entries[1].grid(row=2, column=1)
    entries[2].grid(row=3, column=1)
    entries[3].grid(row=4, column=1)
    back = Button(new_window, text='<', command=new_window.destroy)
    back.grid(row=0, column=0, sticky="nw")
def add():
    newWindow()
    #save_contact = Button(new_window, text='Save', padx=8, pady=3, borderwidth=3, font=('times new roman', 10),
                  # command=lambda: save(entries))
    #save_contact.grid(row=6, column=1, columnspan=2)


def view():
    new_window2 = Toplevel(root)
    new_window2.title('Contacts')

    def delete():
        for entry in entry_list:
            entry.delete(0, END)

    new_window2.title('Contacts')
    entry_list = []

    label = Label(new_window2, text='Contact 1', font=('times new roman', 14))
    name = Label(new_window2, text='Name', font=('times new roman', 12))
    phone = Label(new_window2, text='Phone', font=('times new roman', 12))
    email = Label(new_window2, text='Email', font=('times new roman', 12))
    dob = Label(new_window2, text='DoB', font=('times new roman', 12))
    e5 = Entry(new_window2, width=30)
    e6 = Entry(new_window2, width=30)
    e7 = Entry(new_window2, width=30)
    e8 = Entry(new_window2, width=30)
    delete = Button(new_window2, text='Delete', padx=8, pady=3, borderwidth=3, font=('times new roman', 10),
                    command=delete)
    edit = Button(new_window2, text='Edit', padx=8, pady=3, borderwidth=3, font=('times new roman', 10))
    back = Button(new_window2, text='<', command=root.destroy)

    label.grid(row=0, column=0, columnspan=2)
    name.grid(row=1, column=0)
    phone.grid(row=2, column=0)
    email.grid(row=3, column=0)
    dob.grid(row=4, column=0)
    e5.grid(row=1, column=1)
    e6.grid(row=2, column=1)
    e7.grid(row=3, column=1)
    e8.grid(row=4, column=1)
    delete.grid(row=6, column=2)
    edit.grid(row=6, column=0, columnspan=2)
    back.grid(row=0, column=0, sticky="nw")

    entry_list.append(e5)
    entry_list.append(e6)
    entry_list.append(e7)
    entry_list.append(e8)


label = Label(root, text='Contacts', font=('times new roman', 14))
search = Label(root, text='Search', font=('times new roman', 12))
e = Entry(root, width=30)

add_contact = Button(root, text='+', command=add)
view_contact = Button(root, text='v', command=view)

label.grid(row=0, column=0)
search.grid(row=1, column=0)
e.grid(row=1, column=1)
add_contact.grid(row=0, column=0, columnspan=2)
view_contact.grid(row=1, column=2)

root.mainloop()
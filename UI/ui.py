from mongoConnector import connector
from tkinter import *

root = Tk()
root.title('Phone Book')

def save(entries, window):
    data={'name': entries[0].get(), 'phone': entries[1].get(), 'email': entries[2].get(), 'dob': entries[3].get()}
    print(data)
    connector.saveContact(data)
    window.destroy()
    refreshList()
def update(id, entries, window):
    data = {'name': entries[0].get(), 'phone': entries[1].get(), 'email': entries[2].get(), 'dob': entries[3].get()}
    print(data)
    connector.updateContact(id, data)
    window.destroy()
    refreshList()
def delete(id, window):
    connector.deleteContactUsingID(id)
    window.destroy()
    refreshList()
# using this func to create a secondary contact window
# use case: new contact, edit, view(delete)
def newWindow(usecase: str, data: dict):
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
    entries[0].insert(0, data.get("name", ' '))
    entries[1].insert(0, data.get("phone", ' '))
    entries[2].insert(0, data.get("email", ' '))
    entries[3].insert(0, data.get("dob", ' '))

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
    if usecase=='add':
        save_button=Button(new_window, text='Save', padx=8, pady=3, borderwidth=3, font=('times new roman', 10),
                  command=lambda: save(entries, new_window))
        save_button.grid(row=6, column=1, columnspan=2)
    elif usecase=='view':
        delete_button = Button(new_window, text='Delete', padx=8, pady=3, borderwidth=3, font=('times new roman', 10),
                             command=lambda: delete(data["_id"], new_window))
        delete_button.grid(row=6, column=2)
        edit_button = Button(new_window, text='Edit', padx=8, pady=3, borderwidth=3, font=('times new roman', 10),
                             command=lambda: update(data["_id"], entries, new_window))
        edit_button.grid(row=6, column=0)
def add():
    newWindow("add", {})


def view(id):
    data=connector.fetchSingleContactUsingId(id)
    newWindow("view", data)

contactlist= []
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    global contactlist

    index = w.curselection()[0]
    print('You selected item %d: "%s"' % (index, contactlist[index]))
    view(contactlist[index]['_id'])



def refreshList():
    global contactslistbox
    global contactlist
    contactslistbox.destroy()
    contactslistbox = Listbox(root,
                              bg="grey",
                              activestyle='dotbox',
                              font="Helvetica",
                              fg="yellow")
    contactslistbox.grid(row=3, columnspan=3)
    contactslistbox.bind('<<ListboxSelect>>', onselect)
    contactlist= connector.fetchAllContacts()
    for ele in contactlist:
        contactslistbox.insert(ele['counter'],  ele['name'])


label = Label(root, text='Contacts', font=('times new roman', 14))
search = Label(root, text='Search', font=('times new roman', 12))
e = Entry(root, width=30)
e.bind()



add_contact = Button(root, text='+', command= add)
view_contact = Button(root, text='v', command=view)

label.grid(row=0, column=0)
search.grid(row=1, column=0)
e.grid(row=1, column=1)
add_contact.grid(row=0, column=0, columnspan=2)
view_contact.grid(row=1, column=2)
contactslistbox = Listbox(root,
                          bg="grey",
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="yellow")
refreshList()
root.mainloop()
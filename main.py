from tkinter import *

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin@cluster0.ripustv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client["phone_book"]
coll=db["contacts"]

root = Tk()
root.title('Phone Book')

def saveContact(imp):
    print(f'saving contact for {imp["name"]}')
    saveContactsToMongo(imp)
    print('contact saved')

def ListContacts(searchField:str, searchString:str):
    if searchField=="name":
        return fetchContactUsingName(searchString)
    if searchField=="phone_number":
        return fetchContactUsingPhone(searchString)
    if searchField=="email":
        return fetchContactUsingEmail(searchString)

def saveContactsToMongo(record):
    coll.insert_one(record)

def getContactsFromMongo(query:dict):
    return coll.find(query)

def fetchContactUsingName(imp:str):
    searchQuery={"name":{"$regex":imp}}
    return getContactsFromMongo(searchQuery)

def fetchContactUsingPhone(imp:str):
    searchQuery={"phone_number.$":{"$regex":imp}}
    return getContactsFromMongo(searchQuery)

def fetchContactUsingEmail(imp:str):
    searchQuery={"email.$":{"$regex":imp}}
    return getContactsFromMongo(searchQuery)
def add():

    new_window = Toplevel(root)
    new_window.title('Add New Contacts')
    label = Label(new_window, text='New Contact', font=('times new roman', 14))
    name = Label(new_window, text='Name', font=('times new roman', 12))
    phone = Label(new_window, text='Phone', font=('times new roman', 12))
    newphone = Button(new_window, text='+')
    email = Label(new_window, text='Email', font=('times new roman', 12))
    newemail = Button(new_window, text='+')
    dob = Label(new_window, text='DoB', font=('times new roman', 12))
    e1= Entry(new_window, width=30)
    e2= Entry(new_window, width=30)
    e3= Entry(new_window, width=30)
    e4= Entry(new_window, width=30)
    data={'name':}
    save = Button(new_window, text='Save', padx=8, pady=3, borderwidth=3, font=('times new roman', 10), command=lambda: saveContact())
    back = Button(new_window, text='<', command=new_window.destroy)

    label.grid(row=0, column=0, columnspan=2)
    name.grid(row=1, column=0)
    phone.grid(row=2, column=0)
    newphone.grid(row=2, column=2)
    email.grid(row=3, column=0)
    newemail.grid(row=3, column=2)
    dob.grid(row=4, column=0)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    save.grid(row=6, column=1, columnspan=2)
    back.grid(row=0, column=0, sticky="nw")



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
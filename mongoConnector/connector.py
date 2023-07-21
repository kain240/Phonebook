from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin@cluster0.kdjr66w.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

__db__ = client["phone_book"]
__coll__ = __db__["contacts"]


def saveContact(inp):
    print(f'saving contact for {inp["name"]}')
    __coll__.insert_one(inp)
    print('contact saved')

def updateContact(inp):
    print(f'updating contact for {inp["_id"]}')
    __coll__.update_one({"_id": inp["_id"]}, inp)
    print('contact updated')

def deleteContact(inp):
    print(f'deleting contact for {inp["_id"]}')
    __coll__.delete_one({"_id": inp["_id"]})
    print('contact deleted')

def __getContacts__(query: dict):
    return __coll__.find(query)

def listContacts(searchField: str, searchString: str):
    if searchField == "name":
        return fetchContactUsingName(searchString)
    if searchField == "phone_number":
        return fetchContactUsingPhone(searchString)
    if searchField == "email":
        return fetchContactUsingEmail(searchString)

def fetchContactUsingName(imp: str):
    searchQuery = {"name": {"$regex": imp}}
    return __getContacts__(searchQuery)

def fetchContactUsingPhone(imp: str):
    searchQuery = {"phone_number.$": {"$regex": imp}}
    return __getContacts__(searchQuery)


def fetchContactUsingEmail(imp: str):
    searchQuery = {"email.$": {"$regex": imp}}
    return __getContacts__(searchQuery)

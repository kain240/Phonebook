from pymongo.mongo_client import MongoClient
from bson import ObjectId
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://admin:admin@cluster0.kdjr66w.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient()

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
    if inp['name']==' ':
        inp['name']=''
    if inp['phone']==' ':
        inp['phone']=''
    __coll__.insert_one(inp)
    print('contact saved')

def updateContact(id, inp):
    print(f'updating contact for ', id)
    __coll__.update_one({"_id": ObjectId(id)}, {"$set": inp})
    print('contact updated')

def deleteContactUsingID(id):
    print('deleting contact for ', id)
    __coll__.delete_one({"_id": id})
    print('contact deleted')

def getContacts(query: dict, project: dict):
    cur= __coll__.find(query, project)
    data=[]
    for ele in cur:
        data.append(ele)
    return data

def fetchSingleContactUsingId(id):
    query={'_id': ObjectId(id)}
    return __coll__.find_one(query)

def fetchAllContacts():
    cur=__coll__.find({"name": {"$ne": ""}}, {"name": 1}).sort("name")
    data= []
    for ele in cur:
        data.append(ele)
    cur = __coll__.find({"name": {"$eq": ""}}, {"phone": 1}).sort("phone")
    for ele in cur:
        ele['name'] = ele['phone']
        data.append(ele)
    print(data)
    return data

def listContacts(searchField: str, searchString: str):
    if searchField == "name":
        return fetchContactUsingName(searchString)
    if searchField == "phone_number":
        return fetchContactUsingPhone(searchString)

def fetchContactUsingName(imp: str):
    searchQuery = {"name": {"$regex": imp}}
    return getContacts(searchQuery, {'name': 1})

def fetchContactUsingPhone(imp: str):
    searchQuery = {"phone_number.$": {"$regex": imp}}
    data= []
    cur= getContacts(searchQuery, {'phone': 1})
    for ele in cur:
        ele['name'] = ele['phone']
        data.append(ele)
    return data



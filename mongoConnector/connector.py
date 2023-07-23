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

def getContacts(query: dict):
    cur= __coll__.find(query)
    data=[]
    for ele in cur:
        data.append(ele)
    return data

def fetchSingleContactUsingId(id):
    query={'_id': ObjectId(id)}
    return __coll__.find_one(query)


def fetchAllContacts():
    # todo : if name not present show number
    cur=__coll__.find({})
    data=[]
    counter=0
    for ele in cur:
        counter+=1
        temp={}
        temp['counter']= counter
        temp["_id"]= ele["_id"]
        temp['name']= ele["name"]
        if temp['name']== " ":
            temp['name']=ele['phone']
        data.append(temp)
    print(data)
    return data

def listContacts(searchField: str, searchString: str):
    if searchField == "name":
        return fetchContactUsingName(searchString)
    if searchField == "phone_number":
        return fetchContactUsingPhone(searchString)
    if searchField == "email":
        return fetchContactUsingEmail(searchString)

def fetchContactUsingName(imp: str):
    searchQuery = {"name": {"$regex": imp}}
    return getContacts(searchQuery)

def fetchContactUsingPhone(imp: str):
    searchQuery = {"phone_number.$": {"$regex": imp}}
    return getContacts(searchQuery)


def fetchContactUsingEmail(imp: str):
    searchQuery = {"email.$": {"$regex": imp}}
    return getContacts(searchQuery)


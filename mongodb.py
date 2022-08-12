# BASIC OF PYMONGO
import pymongo
client = pymongo.MongoClient("mongodb+srv://sdr:Nksdr957.@cluster0.2jtjpvd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    'name':'nikhil',
    'email':'sardarnikhil957@gmail.com'
}
data={
    'name':'rahul',
    'email':'sardarnikhil957@gmail.com',
    'roll':1
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(data)
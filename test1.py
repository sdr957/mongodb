# manipulation of collection of database

import pymongo

client = pymongo.MongoClient("mongodb+srv://sdr957:Nksdr957@cluster0.2jtjpvd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client['mydb']
collection=database['collection']
records=collection.find()
for i in records:
    print(i)
print("##############################################################################################################################################")
# filter the records:-

#record=collection.find({'name':'Nikhil sardar'})
#record=collection.find({'product':{'$in':['Affordable AI','Master Program']}}) # here 'product' could be atleast of 'Affordable AI' or 'Master Program'
#record=collection.find({'subject':{'$gt':'e'}})   # {'subject':{'$gt':'e'}} means subject would be greater than e
                                                    #'$gte' : means greater than equal to
                                                    # '$lt' : means less than
                                                    # '$lte' : means leass than equal to
#record=collection.find({'name':'Nikhil sardar','email_id':'sardarnikhil957@gmail.com'}) # "AND conditions" both should be true
#record=collection.find({'$or':[{'product': 'Affordable AI'},{'name':'Nikhil sardar'}]})
collection.update_one({'name':'Nikhil sardar'},{'$set':{'name':'Nikhil kumar'}})
#collection.update_many({'name':'Nikhil sardar'},{'$set':{'name':'Nikhil kumar'}})
record=collection.find({'name':{'$in':['Nikhil kumar','Nikhil sardar']}})
#collection.delete_one({'name':'Nikhil sardar'})
#collection.delete_many({'name':'Nikhil sardar'})
for i in record:
    print(i)
print("###############################################################################################################")


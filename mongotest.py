import pymongo
client = pymongo.MongoClient("mongodb+srv://Sharada_Thota:ammu9118@sharada.lc7tr2w.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "sharada",
    "email" : "bvsarada@gmail.com",
    "surname" : "Thota"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
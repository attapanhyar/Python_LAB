from datetime import datetime
import pymongo
from pymongo import MongoClient
import datetime
cluster = MongoClient('mongodb://<ID>:<Password>@cluster0-')
db = cluster['test']
collection = db['test']
# all_dbs = cluster.list_database_names()
# for db in all_dbs:
#     print(db)
all_cols = db.list_collection_names()

print('************* LIST COLLECTiONS')
for col in all_cols:
    print(col)

# post = {"_id":2,"name":"Ali","score":70}
# post1 = {"_id":3,"name":"Ahemd","score":60}
# post2 = {"_id":4,"name":"Shahbaz","score":90}
# collection.insert_many([post,post1,post2])

##############find_one() vs find()
results = collection.find_one({"tags":"Codeing"})
print(results)

################# delete
#collection.delete_one({"_id":1})


# todo = {"name":"Atta", "text":"my first todo", "status":"Open",
#         "tags":["python","Codeing"],"date":datetime.datetime.utcnow()    }
# collection.insert_one(todo)

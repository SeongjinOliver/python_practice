from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.ykr9q.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# doc = {
#     'name': 'bob',
#     'age': 27
# }
# db.users.insert_one(doc)
# db.users.insert_one({'name': 'bobby', 'age': 27})
# db.users.insert_one({'name': 'john', 'age': 20})
# db.users.insert_one({'name': 'ann', 'age': 20})

# all_users = list(db.users.find({},{'_id':False}))
# for user in all_users:
#     print(user)

# user = db.users.find_one({'name': 'bobby'})
# print(user['age'])

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
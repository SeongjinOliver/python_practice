from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.ykr9q.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# # Quiz 1
# movie = db.movies.find_one({'title': '가버나움'})
# print(movie['star'])
#
# # Quiz 2
# all_movies = list(db.movies.find({'star': movie['star']}, {'_id': False}))
# for m in all_movies:
#     print(m['title'])

# Quiz 3
update_movie = db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})


import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient["f4q_crawler"]
mycol = mydb["users"]

# mydb.mycol.drop()
cnt = mycol.find().count()
print(cnt)

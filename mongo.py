import pymongo
import urllib

client = pymongo.MongoClient("mongodb+srv://mongo_user_1:"+ urllib.quote("<PASSWORD>") +"@cluster0-jge7w.mongodb.net/test?retryWrites=true")
mydb = client.test

mycol = mydb["customer"]

for x in mycol.find({"address":"Highway 37"},{"_id":0}):
	print x
	
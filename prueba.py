import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers2"]

myquery = { "age": { "$gt":3} }

mydoc = mycol.find(myquery).min({"age":25})

print("x")

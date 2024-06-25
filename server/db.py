from flask import Flask, request, jsonify
import pymongo

# connection string
mongo_uri = "mongodb+srv://sasindusathiska:Pass123@cluster0.glb4eyt.mongodb.net/?retryWrites=true&w=majority"

try:
   mongo = pymongo.MongoClient(mongo_uri)
   db = mongo.get_database('todo')
   mongo.server_info()   # trigger exeption if connection failed
   
   print("Connected successfully!!!")

except Exception as ex:
        print(ex)
        
        
        
      
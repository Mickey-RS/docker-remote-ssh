from pymongo import MongoClient
try:
    HOST = GIT_HOST
except:
    from config.keys import creds
    HOST = creds['HOST']
    

conn = MongoClient(HOST)
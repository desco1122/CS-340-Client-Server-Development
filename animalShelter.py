from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

    def __init__(self, USER, PASS):

        #USER = 'aacuser'
        #PASS = 'SNHU1234'  
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31328  
        DB = 'AAC'
        COL = 'animals'

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

        print("Connection Successful")

# Create Method for crud.
    def create(self, data):
        
        try:
            if data is not None:
                self.database.animals.insert_one(data)
                return True
            
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                return False
             
        except Exception as e:
            print("An exception occurred ::", e)

# Read method in crud.
    def read(self, readdata):
        try:
            if readdata is not None:
                query = list(self.database.animals.find(readdata, {"_id":False}))
                print("Read Code Reached")
                return query
            else:
                return {}
             
        except Exception as e:
            print("An exception occurred ::", e)
        
# Update method in crud.
    def update(self, readData, updateData):
        try:
            if readData is not None:
                index_update = self.database.animals.update(readData, {"$set":updateData})
                return index_update
            
            else:
                return {}
               
        except Exception as e:
            print("An exception occurred ::", e)       


# Delete method in crud.
    def delete(self, data):
        try:
            if data is not None:
                delete= self.database.animals.delete_many(data)
                return delete
                          
            else:
                return {}
              
        except Exception as e:
            print("An exception occurred ::", e)
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://jayanthkorupolu2004:narmada143@cluster0.kqfqh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Change connection URL if needed
db = client["nuti_db"]  # Create or connect to a database
collection = db["Registration_collection"] 
collection2 = db["User_Accounts"] # Create or connect to a collection


def insert_data(data , name):


    if collection.find_one({"name" : name}) is None:
        insert_result = collection.insert_one({"name" : name , "history" : [data["message"]]})
    else:
        ret_data = collection.find_one({"name": name})
        ret_history = ret_data["history"]
        ret_history.append(data["message"])
        insert_result = collection.update_one({"name" : name}, {"$set": {"history": ret_history}})      


def get_data(name):

    data = collection.find_one({"name": name})

    return data  

def delete_data(name):

    collection.delete_one({"name" : name})



def inser_user_structured_data(data):

    insert_result = collection2.insert_one(data)







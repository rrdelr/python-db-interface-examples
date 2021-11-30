from pymongo import MongoClient

client = MongoClient\
    ("CONNECT#HERE")

# db = database
# col = collection

# Insert one
def insert_one(db, col, item):
    db = client[db]
    col = db[col]
    x = col.insert_one(item)

# Upsert
def insert_one_replacement(db, col, item, conditional):
    db = client[db]
    col = db[col]
    x = col.replace_one(conditional, item, True)

# Insert multi
def insert_multi(db, col, items):
    db = client[db]
    col = db[col]
    x = col.insert_many(items)

# Conditional retrieve
def retrieve(db, col, query, views={}):
    db = client[db]
    col = db[col]
    x = col.find(query, views)
    return(list(x))

# Retrieve all
def retrieve_all(db, col):
    db = client[db]
    col = db[col]
    x = col.find()
    return(list(x))
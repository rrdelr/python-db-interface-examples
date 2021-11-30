from pymongo import MongoClient

class MongoHandler:

    def __init__(self, client_address):
        self.client = MongoClient(client_address)
        # db = database
        # col = collection

    # Insert one
    def insert_one(self, db, col, item):
        db = self.client[db]
        col = db[col]
        x = col.insert_one(item)

    # Upsert
    def insert_one_replacement(self, db, col, item, conditional):
        db = self.client[db]
        col = db[col]
        x = col.replace_one(conditional, item, True)

    # Insert multi
    def insert_multi(self, db, col, items):
        db = self.client[db]
        col = db[col]
        x = col.insert_many(items)

    # Conditional retrieve
    def retrieve(self, db, col, query, views={}):
        db = self.client[db]
        col = db[col]
        x = col.find(query, views)
        return(list(x))

    # Retrieve all
    def retrieve_all(self, db, col):
        db = self.client[db]
        col = db[col]
        x = col.find()
        return(list(x))

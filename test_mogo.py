from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://dilshanish123_db_user:<password>@cluster.jky4rq1.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
from dotenv import load_dotenv
from os import environ
from pymongo import MongoClient


def get_connection():
    load_dotenv()

    client = MongoClient(
        "mongodb://{0}:{1}@{2}:{3}".format(
            environ.get("MONGODB_USERNAME"),
            environ.get("MONGODB_PASSWORD"),
            environ.get("MONGODB_HOST"),
            environ.get("MONGODB_PORT"),
        )
    )

    return client[environ.get("MONGODB_DATABASE")]


if __name__ == "__main__":
    connection = get_connection()
    status = connection["momoStatus"].find_one({"name": "Completed"})

    print(connection)
    print(status)

from dotenv import load_dotenv
from os import environ
from mysql.connector import connect


def get_connection():
    load_dotenv()

    return connect(
        host=environ.get("MYSQL_HOST"),
        port=environ.get("MYSQL_PORT"),
        user=environ.get("MYSQL_USERNAME"),
        password=environ.get("MYSQL_PASSWORD"),
        database=environ.get("MYSQL_DATABASE"),
    )


if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("select * from momoStatus where name = %s", ("Completed",))

    status = cursor.fetchone()

    print(connection)
    print(status)

    cursor.close()

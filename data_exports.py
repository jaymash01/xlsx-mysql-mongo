from datetime import timezone
from mysql_connection import get_connection as get_mysql_connection
from mongo_connection import get_connection as get_mongo_connection

mysql_connection = get_mysql_connection()
mongo_connection = get_mongo_connection()


def export_draws():
    print("Exporting draws...")

    collection = mongo_connection["draw"]
    cursor = mysql_connection.cursor()
    cursor.execute("select * from draw order by id asc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        document = {
            "__id": row[0],
            "createdDate": row[1].astimezone(tz=timezone.utc) if row[1] is not None else None,
            "numberOfTheDay": row[2],
            "isActive": row[3],
            "_class": "com.fasthub.pesafasta.model.Draw",
        }

        collection.insert_one(document)

    cursor.close()
    print("Exported draws successfully...")


def export_rtp_calculations():
    print("Exporting RTP calculations...")

    collection = mongo_connection["rtp"]
    cursor = mysql_connection.cursor()
    cursor.execute("select * from rtp order by createdAt asc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        document = {
            "__id": row[0],
            "createdAt": row[1].astimezone(tz=timezone.utc) if row[1] is not None else None,
            "collection": row[2],
            "payout": row[3],
            "rtp": row[4],
            "_class": "com.fasthub.pesafasta.model.Rtp",
        }

        collection.insert_one(document)

    cursor.close()
    print("Exported  RTP calculations successfully...")


def export_players():
    print("Exporting players...")

    partner = mongo_connection["partner"].find_one({"paybillNumber": "188818"})
    collection = mongo_connection["player"]
    cursor = mysql_connection.cursor()
    cursor.execute("select * from player where date(createdDate) >= '2023-01-01' order by id asc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        document = {
            "__id": row[0],
            "msisdn": row[1],
            "operator": row[2],
            "createdDate": row[3].astimezone(tz=timezone.utc) if row[3] is not None else None,
            "lastPlayedDate": row[4].astimezone(tz=timezone.utc) if row[4] is not None else None,
            "partner": partner,
            "_class": "com.fasthub.pesafasta.model.Player",
        }

        collection.insert_one(document)

    cursor.close()
    print("Exported players successfully...")


def export_mobile_money():
    print("Exporting mobile money...")

    collection = mongo_connection["mobileMoney"]
    cursor = mysql_connection.cursor()
    cursor.execute(
        "select mm.*, st.name as status, tt.name as transactionType from mobileMoney as mm inner join momoStatus as st on mm.statusId = st.id inner join transactionType as tt on mm.transactionTypeId = tt.id order by mm.id asc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        status = mongo_connection["momoStatus"].find_one({"name": row[17]})
        transaction_type = mongo_connection["transactionType"].find_one({"name": row[18]})
        player = mongo_connection["player"].find_one({"__id": row[14]})

        print(status)
        print(transaction_type)
        print(player, end="\n\n")

        if player is not None:
            document = {
                "__id": row[0],
                "createdDate": row[1].astimezone(tz=timezone.utc) if row[1] is not None else None,
                "company": row[2],
                "operator": row[3],
                "txnId": row[4],
                "paybillNumber": row[5],
                "receipt": row[6],
                "msisdn": row[7],
                "amount": row[8],
                "reference": row[9],
                "country": row[10],
                "numberChoice": row[11],
                "status": status,
                "transactionType": transaction_type,
                "player": player,
                "processed": row[15],
                "description": row[16],
                "_class": "com.fasthub.pesafasta.model.MobileMoney",
            }

            collection.insert_one(document)

    cursor.close()
    print("Exported mobile money successfully...")


def export_transactions():
    print("Exporting transactions...")

    collection = mongo_connection["transaction"]
    cursor = mysql_connection.cursor()
    cursor.execute("select * from transaction order by id asc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        player = mongo_connection["player"].find_one({"__id": row[6]})
        mobile_money = mongo_connection["mobileMoney"].find_one({"__id": row[7]})
        draw = mongo_connection["draw"].find_one({"__id": row[8]})

        print(player)
        print(mobile_money)
        print(draw, end="\n\n")

        if player is not None and mobile_money is not None and draw is not None:
            document = {
                "__id": row[0],
                "ticket": row[1],
                "numberOfTheDay": row[2],
                "jackpotNumber": row[3],
                "createdDate": row[4].astimezone(tz=timezone.utc) if row[4] is not None else None,
                "updatedDate": row[5].astimezone(tz=timezone.utc) if row[5] is not None else None,
                "player": player,
                "mobileMoney": mobile_money,
                "draw": draw,
                "isPaid": row[9],
                "numberChoice": row[10],
                "winningAmount": row[11],
                "payoutAmount": row[12],
                "luckNumberId": row[13],
                "createdAt": row[14].astimezone(tz=timezone.utc) if row[14] is not None else None,
                "_class": "com.fasthub.pesafasta.model.Transaction",
            }

            collection.insert_one(document)

    cursor.close()
    print("Exported transactions successfully...")

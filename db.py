import pymysql.cursors
import sys


def db_add_data(chat_id, user_id, message_id, anger, anxiety, happiness, sadness, date):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='EAB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `data` (`chat_id`, `user_id`, `message_id`, `anger`, `anxiety`, `happiness`, `sadness`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s, from_unixtime(%s))"
            cursor.execute(sql, (chat_id, user_id, message_id, anger, anxiety, happiness, sadness, date))
            result = cursor.fetchone()
            print(result)
            connection.commit()
    except Exception:
        print(sys.exc_info())

    connection.close()



def db_read_data(user_id):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='EAB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT round(avg(`anger`),3) as average_anger_is, round(avg(`anxiety`),3) as average_anxiety_is, round(avg(`happiness`),3) as average_happiness_is, round(avg(`sadness`),3) as average_sadness_is  FROM `data` WHERE `user_id`= %s"
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
            print(result)
            connection.commit()
    except Exception:
        print(sys.exc_info())

    return result
    connection.close()


     
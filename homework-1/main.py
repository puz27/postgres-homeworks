"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2


# my_connection = psycopg2.connect(
#     host="localhost",
#     database="test",
#     user="postgres",
#     password="y00ddaev"
# )
#
# cursor = my_connection.cursor()
# #cursor.execute("INSERT INTO town (id, size) VALUES(12, 1000)")
# #cursor.execute("INSERT INTO town (id, size) VALUES(333, 1000)")
# #cursor.executemany("INSERT INTO town (id, size) VALUES (%s, %s)", [(20, "Данные"), (19, "Другие")])
# my_connection.commit()
#
#
# cursor.execute("select * from town")
# rows = cursor.fetchall()
# print(rows)
# cursor.close()
# my_connection.close()

connector = psycopg2.connect(
host="localhost",
database="test",
user="postgres",
password="y00ddaev"
)

try:
    with connector:
        with connector.cursor() as cursor:
            cursor.execute("INSERT INTO town (id, size) VALUES(30, 1000)")
            cursor.execute("select * from town")
            get = cursor.fetchall()
            print(get)
finally:
    connector.close()







"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def get_data_csv(path):
    data = []
    try:
        with open(path) as csv_file:
            take_csv_data = csv.reader(csv_file, delimiter=",")
            count = 0
            for roe in take_csv_data:
                if count != 0:
                    data.append(roe)
                count += 1
    except FileNotFoundError:
        print("File not found!")
    return data


customers_data = get_data_csv("north_data/customers_data.csv")
orders_data = get_data_csv("north_data/orders_data.csv")
employees_data = get_data_csv("north_data/employees_data.csv")


def send_query(table, args):
    connection = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="y00ddaev"
    )

    try:
        with connection.cursor() as cursor:
            col_count = "".join("%s," * len(args[0]))
            query = f"INSERT INTO {table} VALUES ({col_count[:-1]})"
            cursor.executemany(query, args)
            connection.commit()
    # except psycopg2.Error:
    #     print("Ошибка с запросом.")
    finally:
        connection.close()


send_query("customers", customers_data)
send_query("orders", orders_data)
send_query("employees", employees_data)






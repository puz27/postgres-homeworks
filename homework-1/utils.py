import psycopg2
import csv


def get_data_csv(path: str) -> list:
    """
    Get data from file.
    :param path: Path to file with datas.
    :return List with datas from file.
    """
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


def send_query(table: str, args: list, user: str, password: str) -> None:
    """
    Send SQL queries to Data Base north on localhost
    :param table: Name of table in database.
    :param args: List of data for adding.
    :param user: User name connection.
    :param password: Password user for connection.
    """
    connection = psycopg2.connect(
        host="localhost",
        database="north",
        user=user,
        password=password
    )
    try:
        with connection:
            with connection.cursor() as cursor:
                col_count = "".join("%s," * len(args[0]))
                query = f"INSERT INTO {table} VALUES ({col_count[:-1]})"
                cursor.executemany(query, args)
                connection.commit()
                print(f"Операция над таблицей {table} прошла успешно.")
    except psycopg2.Error:
        print("Ошибка с запросом.")
    finally:
        connection.close()

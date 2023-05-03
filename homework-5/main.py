import json
import psycopg2
from config import config
import os


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'my_new_db'

    params = config()
    conn = None

    create_database(params, db_name)

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                # create_suppliers_table(cur)
                # print("Таблица suppliers успешно создана")
                #
                # suppliers = get_suppliers_data(json_file)
                # insert_suppliers_data(cur, suppliers)
                # print("Данные в suppliers успешно добавлены")
                #
                # add_foreign_keys(cur, json_file)
                # print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""
    connection = psycopg2.connect(**params)
    connection.autocommit = True
    try:
        with connection.cursor() as cursor:
            query_create_base = f"CREATE DATABASE {db_name}"
            cursor.execute(query_create_base)
            print(f"База данных {db_name} успешно создана.")
    except psycopg2.Error as er:
        print(f"БД:{db_name}. Ошибка с запросом создания БД.\n{er}")
    finally:
        connection.close()


def execute_sql_script(cur, script_file) -> None:
    path_file = os.path.join(os.getcwd(), script_file)
    file = open(path_file, 'r', encoding='utf-8')
    query_create_base = file.read()
    file.close()
    cur.execute(query_create_base)


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


# def get_suppliers_data(json_file: str) -> list[dict]:
#     """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
#     pass


# def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
#     """Добавляет данные из suppliers в таблицу suppliers."""
#     pass


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    pass


if __name__ == '__main__':
    main()

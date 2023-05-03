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

    #create_database(params, db_name)

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # execute_sql_script(cur, script_file)
                # print(f"БД {db_name} успешно заполнена")

                # create_suppliers_table(cur)
                # print("Таблица suppliers успешно создана")

                suppliers = get_suppliers_data(json_file)
                insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")
                #
                # add_foreign_keys(cur, json_file)
                # print(f"FOREIGN KEY успешно добавлены")
                conn.commit()
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

    query = """CREATE TABLE suppliers (
    company_name VARCHAR(100),
    contact VARCHAR(100),
    address VARCHAR(100),
    phone VARCHAR(100),
    fax VARCHAR(100),
    homepage VARCHAR(100),
    products VARCHAR(100));
    """
    cur.execute(query)



def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    path_file = os.path.join(os.getcwd(), json_file)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""
    col_count = "".join("%s," * 7)
    query = f"INSERT INTO suppliers VALUES ({col_count})"

    data = []
    all_data = []
    for i in suppliers:
        data.append(i["company_name"])
        data.append(i["contact"])
        data.append(i["address"])
        data.append(i["phone"])
        data.append(i["fax"])
        data.append(i["homepage"])
        data.append(str(i["products"]))
        all_data.append(data)
    print(all_data)
    #cur.executemany(query, all_data)


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    pass


if __name__ == '__main__':
    main()

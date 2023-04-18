from utils import get_data_csv, send_query


def main():

    user = input("Input user\n")
    password = input("Input password\n")

    customers_data = get_data_csv("north_data/customers_data.csv")
    orders_data = get_data_csv("north_data/orders_data.csv")
    employees_data = get_data_csv("north_data/employees_data.csv")

    send_query("customers", customers_data, user, password)
    send_query("orders", orders_data, user, password)
    send_query("employees", employees_data, user, password)


if __name__ == '__main__':
    main()





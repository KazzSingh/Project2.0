from menu import main_menu
from products import product_menu
from couriers import courier_menu
from orders import order_menu
from sql_read_write import load_data, save_data
import pprint

products, couriers, customers, orders, order_status_options = load_data()

while True:
    main_request = main_menu()
    if main_request == "0":
        save_data(products, couriers, orders)
        break
    elif main_request == "1":
        products = product_menu(products)
    elif main_request == "2":
        couriers = courier_menu(couriers)
    elif main_request == "3":
        orders = order_menu(customers, orders, order_status_options, couriers)
    else:
        print("Invalid option")



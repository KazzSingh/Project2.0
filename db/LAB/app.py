from menu import main_menu
from customers import customer_menu
from products import product_menu
from couriers import courier_menu
from orders import order_menu
from sql_read_write import save_data


while True:
    main_request = main_menu()
    if main_request == "0":
        break
    elif main_request == "1":
        product_menu()
    elif main_request == "2":
        courier_menu()
    elif main_request == "3":
        customer_menu()
    elif main_request == "4":
        order_menu()
    else:
        print("Invalid option")

from utils import print_with_index
import sql_read_write as sql


def _get_order_request():
    print()
    print("Order menu options:")
    print("  0: Return to main menu")
    print("  1: Display orders")
    print("  2: Create new order")
    print("  3: Update existing order status")
    print("  4: Update existing order")
    print("  5: Delete existing order")
    print()
    order_request = input("Select option (0, 1, 2, 3, 4, 5): ")
    return order_request


def _create_new_order(customers, orders, couriers):
    customers, cust_id = _create_new_customer_id(customers)
    order = {}
    order["cust_id"] = cust_id
    print("Available couriers:")
    print_with_index(couriers)
    order["courier"] = courier = couriers[int(
        input("Courier index: "))]['courier_ID']
    values = cust_id, courier
    # basket = []
    # while pick.lower != 'x':
    #     pick = input("Please pick an item index to add to basket or press x to end")
    #     order["basket"] = basket
    order_id = sql.insert_new_order(values)
    order["order_id"] = order_id
    order["status"] = "preparing"
    orders.append(order)
    return customers, orders


def _create_new_customer_id(customers):
    customer = {}
    customer['cust_ID'] = ''
    customer["f_name"] = f_name = input("Customer's first name: ")
    customer["l_name"] = l_name = input("Last name: ")
    customer["flo_address"] = flo_address = input(
        "First line of address: ")
    customer["postcode"] = postcode = input("Postcode: ")
    customer["cust_phone"] = cust_phone = input("Customer phone number: ")
    values = f_name, l_name, flo_address, postcode, cust_phone
    # inserts into table and returns cust_id
    cust_id = sql.insert_new_customer(values)
    customer['cust_ID'] = cust_id
    customers.append(customer)
    return customers, cust_id


def _update_existing_order_status(orders, order_status_options):
    print_with_index(orders)
    order_index = int(input("Order index: "))
    print_with_index(order_status_options)
    order_status_index = int(input("Order status index: "))
    orders[order_index]["status"] = order_status_options[order_status_index]
    return orders


def _update_existing_order(orders):
    print_with_index(orders)
    order_index = int(input("Order index: "))
    # this creates a reference to the order inside the list
    order = orders[order_index]
    for key in order.keys():
        new_value = input(f"New value for '{key}': ")
        if new_value:
            order[key] = new_value
    return orders


def _delete_existing_order(orders):
    print_with_index(orders)
    order_index = int(input("Order index: "))
    orders.pop(order_index)
    return orders


def order_menu(customers, orders, order_status_options, couriers):
    order_request = None
    while order_request != "0":
        order_request = _get_order_request()
        if order_request == "0":
            return orders
        elif order_request == "1":
            print(orders)
        elif order_request == "2":
            customers, orders = _create_new_order(customers, orders, couriers)
        elif order_request == "3":
            orders = _update_existing_order_status(
                orders, order_status_options)
        elif order_request == "4":
            orders = _update_existing_order(orders)
        elif order_request == "5":
            orders = _delete_existing_order(orders)
        else:
            print("Invalid option")

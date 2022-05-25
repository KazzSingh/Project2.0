from utils import print_with_index
import sql_read_write as sql
import customers as cs
import inputs as take


def get_order_request():
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


def get_update_order_request():
    print()
    print("Update Order menu options:")
    print("  0: Return to orders menu")
    print("  1: Edit Customer details")
    print("  2: Choose a new Courier")
    # 'ADD to your basket feature coming soon!'*
    print("  3: Replace basket items")
    print("  4: Update existing order status")
    print()
    update_order_request = input("Select option (0, 1, 2, 3): ")
    return update_order_request


def create_new_order():
    cust_id = cs.new_or_existing_cust()
    print("Available couriers:")     # pick courier by index, return courier ID
    couriers = sql.print_couriers()
    courier_id = couriers[take.valid_index(
        couriers, input("Courier INDEX: "))]['courier_id']
    basket = add_items_to_basket()
    order_status = "preparing"     # default order status - upload to order table
    values = cust_id, courier_id, basket, order_status
    order_id = sql.insert_new_order(values)
    print("\n Order added Successfully")


def add_items_to_basket():
    basket = []  # pick items for the order and populate a list - will update to take quantity
    products = sql.print_products()
    pick = input(
        "\nPlease pick an item INDEX to add to basket or any other character to complete order: ")
    while pick.isdigit():
        try:
            basket.append(str(products[int(pick)]['product_id']))
            pick = input(
                "\n Add another item INDEX to add to basket or press any other character to complete order: ")
        except IndexError:
            pick = input(
                "\n Please pick a valid item INDEX to add to basket or press any other character to complete order: ")
            print_products()
            print("\n")
    basket = ",".join(basket)
    return basket


def update_existing_order_status(order_index):
    orders = sql.get_orders_dict()
    order_status_options = ["preparing", "sent", "delivered", "cancelled"]
    print_with_index(order_status_options)
    order_status_index = int(input("Order status INDEX: "))
    orders[order_index]['order_status'] = order_status_options[order_status_index]
    print("\nOrder status successfuly updated.")
    # change this to ammend the database instead of this list
    # orders[order_index]["status"] = order_status_options[order_status_index] NEEDS TO BE CHANGED TO UPDATE THE SQL RECORD


def update_existing_order():
    orders = sql.print_orders()
    order_index = int(
        input("\n INDEX of the order you would like to update: "))

    update_order_request = None
    while update_order_request != "0":
        update_order_request = get_update_order_request()
        if update_order_request == "0":
            return
        elif update_order_request == "1":
            # update_existing_customer ########################################################################
            customers = sql.get_customers_dict()
            for i, customer in enumerate(customers):
                cust_id, f_name, l_name, flo_address, postcode, cust_phone = customer.values()
                if customer['cust_id'] == orders[order_index]['cust_id']:
                    sql.print_specific_customer(customer['cust_id'])
                    cs.update_existing_customer(i)
                    ###########################################################################################
        elif update_order_request == "2":
            # choosing a new courier ######################### ######################## #######################
            sql.print_specific_courier(orders[order_index]['courier_id'])
            print("\nPlease select an index from the following couriers:\n ")
            couriers = sql.print_couriers()
            courier_index = int(input("\nIndex: "))
            orders[order_index]['courier_id'] = couriers[courier_index]['courier_id']
            values = orders[order_index]['courier_id'], orders[order_index]['basket'], orders[order_index]['order_id']
            sql.update_order_rec(values)
            ####################### ######################### ######################## ########################
        elif update_order_request == "3":
            # replacing the basket with new items #############################################################
            print("\nBasket emptied. Please select items from the list below. \n")
            basket = add_items_to_basket()
            values = orders[order_index]['courier_id'], basket, orders[order_index]['order_id']
            sql.update_order_rec(values)
            ###################################################################################################
        elif update_order_request == "4":
            update_existing_order_status(order_index)
        else:
            print("Invalid option")


def delete_existing_order():
    orders = sql.print_orders()
    order_index = input("\n INDEX of the order you would like to delete: ")
    sql.delete_order_rec(orders[int(order_index)]['order_id'])


def order_menu():
    order_request = None
    while order_request != "0":
        order_request = get_order_request()
        if order_request == "0":
            return
        elif order_request == "1":
            sql.print_orders()
        elif order_request == "2":
            create_new_order()
        elif order_request == "3":
            sql.print_orders()
            order_index = int(input("Order INDEX: "))
            update_existing_order_status(order_index)
        elif order_request == "4":
            update_existing_order()
        elif order_request == "5":
            delete_existing_order()
        else:
            print("Invalid option")

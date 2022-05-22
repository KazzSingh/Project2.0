import config as cnfg
import main
import products as pm
import couriers as cm
import orders as om
# import unittest

product_list = []
courier_list = []
order_list = []

main_menu = ["Exit", "Product Menu Options",
             "Courier Menu Options", "Order Menu Options"]

product_menu = ["Return to Main Menu", "Product List", "Create new Product!",
                "Update existing Product!", "Delete Product"]


# # ###########################################################################################

# def run_create_sequence():
#     cnfg.print_line_break()
#     create_item()
#     pm.run_product_sequence()

# ###########################################################################################


def create_item():
    new_product = {}
    item = product_name()
    price = product_price()
    new_product["name"] = item.upper()
    new_product["price"] = (price)
    product_list.append(new_product)

    create_item()


def product_name():
    item_name = input(
        "\n Enter the name of the product you would like to add to the inventory, or '0' to go back to the product menu: ")
    if product_name == "0":
        pm.run_product_sequence()
    elif item_name.isdigit():
        print("\n Please enter a valid product name")
        product_name()
    elif confirm_choice(item_name):
        return item_name
    else:
        return run_create_sequence()


def product_price(item_price):
    try:
        if confirm_choice(float(item_price), "£"):
            print("success")
            item_price = (float(item_price))
            return item_price
        elif item_price.lower() == 'x':
            return 'run_product_sequence()'
    except:
        return "not valid, please enter the price in the following format (0.00)"
    # product_name()

    # ###########################################################################################

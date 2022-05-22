import config as cnfg


product_menu = ["Return to Main Menu", "Product List", "Create new Product",
                "Update existing Product", "Delete Product"]

product_list = [{'name': 'apples', 'price': '2.99'},
                {'name': 'cake', 'price': '2.00'}]


def run_product_sequence():
    cnfg.print_line_break()
    cnfg.print_options(product_menu)
    navigate_product_menu()


###########################################################################################

def navigate_product_menu():
    user_input = input('''
Please pick from the following options below using the index number shown \n
Enter option index here:
    ''')
    if user_input == "0":
        return
    elif user_input == "1":
        run_view_products()
        run_product_sequence()
    elif user_input == "2":
        run_create_sequence()
        run_product_sequence()
    elif user_input == "3":
        # run_update_sequence()
        run_product_sequence()
    elif user_input == "4":
        # run_delete_sequence()
        run_product_sequence()
    else:
        print("please pick a valid option... try to use digits only and no other letters or characters. ")
        run_product_sequence()


# ###########################################################################################

def run_view_products():
    cnfg.print_line_break()
    cnfg.print_options(product_list)
    print("\n You can make changes to this list from the product menu")


# # ###########################################################################################

def run_create_sequence():
    cnfg.print_line_break()
    create_item()
    pm.run_product_sequence()

# ###########################################################################################


def create_item():
    new_product = {}
    item = product_name()
    price = product_price()
    new_product["name"] = item.title()
    new_product["price"] = price
    product_list.append(new_product)
    print(product_list)
    print('\n Lets go again... ')
    create_item()

# ###########################################################################################


def product_name():
    item_name = input(
        "\n Enter the name of the product you would like to add to the inventory, or '0' to go back to the product menu: ")
    if product_name == "0":
        run_product_sequence()
    elif item_name.isdigit():
        print("\n Please enter a valid product name")
        product_name()
    elif cnfg.confirm_choice(item_name):
        return item_name
    else:
        return run_create_sequence()

# ###########################################################################################


def product_price():
    item_price = input(
        "\n Please enter the price of the item in the following format e.g. '0.00' or press 'x' to exit: ")
    try:
        if cnfg.confirm_choice(item_price, "£"):
            print("\n Okay, success.")
            item_price = (float(item_price))
            return item_price
        elif item_price.lower() == 'x':
            return 'run_product_sequence()'
    except:
        return "\n not valid, please enter the price in the following format (0.00)"
    product_name()

# ###########################################################################################

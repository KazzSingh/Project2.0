import config

product_menu = ["Return to Main Menu", "Product List", "Create new Product!",
                "Update existing Product!", "Delete Product"]


product_list = []


def run_product_sequence():
    print_line_break()
    print_options(product_menu)
    navigate_product_menu()

###########################################################################################


def navigate_product_menu():

    user_input = input("\n Enter option index here: ")

    if user_input == "0":
        run_main_menu()
    elif user_input == "1":
        run_view_products()
    elif user_input == "2":
        run_create_sequence()
    elif user_input == "3":
        run_update_sequence()
    elif user_input == "4":
        run_delete_sequence()
    else:
        print("please pick a valid option... try to use digits only and no other letters or characters. ")
        run_product_menu()

# ###########################################################################################


def run_view_products():
    print_line_break()
    print_options(product_list)
    print("\n You can make changes to this list from the product menu")

# ###########################################################################################


def run_create_sequence():
    print_line_break()
    create_item()
    run_create_sequence()

# ###########################################################################################


def create_item():
    new_product = {}
    product_name = input(
        "\n Enter the name of the product you would like to add to the inventory, or '0' to go back to the product menu: ")
    if product_name != "0" and confirm_choice(product_name):
        product_price = float(input(
            "Excellent, before I add it to the inventory, please enter the price of that new item, or press X to exit: "))
        if product_price != "X" and confirm_choice(product_price, "£"):
            print(
                f"\n {new_product} has been added to the inventory at the cost of £{product_price} \n")
            new_product["name"] = product_name
            new_product[price] = product_price
            product_list.append(new_product)
    return

    # ###########################################################################################


def confirm_choice(choice, currency_symbol=""):
    confirm = input(
        f"{currency_symbol}{choice}? Are you sure? enter [1] for yes, [any other key] for no: ")
    if confirm == "1":
        return True
    else:
        return False


run_product_sequence()
print(product_list)

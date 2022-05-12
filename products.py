import config as cnfg

product_menu = ["Return to Main Menu", "Product List", "Create new Product!",
                "Update existing Product!", "Delete Product"]

product_list = []


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
        # run_create_sequence()
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

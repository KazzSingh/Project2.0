import config as cnfg

order_menu = ["Return to Main Menu", "Order List", "Create New Order!", "Update Order Status",
              "Update Existing Order!", "Delete Order"]

order_list = []


def run_order_sequence():
    cnfg.print_line_break()
    cnfg.print_options(order_menu)
    navigate_order_menu()


# ###########################################################################################

def navigate_order_menu():
    user_input = input('''
Please pick from the following options below using the index number shown \n 
Enter option index here: 
    ''')
    if user_input == "0":
        return
    elif user_input == "1":
        run_view_orders()
        run_order_sequence()
    elif user_input == "2":
        # run_create_sequence()
        run_order_sequence()
    elif user_input == "3":
        # run_update_orderstatus_sequence()
        run_order_sequence()
    elif user_input == "4":
        # run_update_sequence()
        run_order_sequence()
    elif user_input == "5":
        # run_delete_sequence()
        run_order_sequence()
    else:
        print("please pick a valid option... try to use digits only and no other letters or characters. ")
        run_order_menu()


# ###########################################################################################

def run_view_orders():
    cnfg.print_line_break()
    cnfg.print_options(order_list)
    print("\n You can make changes to this list from the order menu")

import config as cnfg

courier_menu = ["Return to Main Menu", "Courier List", "Create new Courier!",
                "Update existing Courier!", "Delete Courier"]

courier_list = []


def run_courier_sequence():
    cnfg.print_line_break()
    cnfg.print_options(courier_menu)
    navigate_courier_menu()


# ###########################################################################################

def navigate_courier_menu():
    user_input = input('''
Please pick from the following options below using the index number shown \n 
Enter option index here: 
    ''')
    if user_input == "0":
        return
    elif user_input == "1":
        run_view_couriers()
        run_courier_sequence()
    elif user_input == "2":
        # run_create_sequence()
        run_courier_sequence()
    elif user_input == "3":
        # run_update_sequence()
        run_courier_sequence()
    elif user_input == "4":
        # run_delete_sequence()
        run_courier_sequence()
    else:
        print("please pick a valid option... try to use digits only and no other letters or characters. ")
        run_courier_menu()


# ###########################################################################################

def run_view_couriers():
    cnfg.print_line_break()
    cnfg.print_options(courier_list)
    print("\n You can make changes to this list from the courier menu")

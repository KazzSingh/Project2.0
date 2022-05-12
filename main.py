import config as cnfg
import products as pm
import couriers as cm
import orders as om


main_menu = ["Exit", "Product Menu Options",
             "Courier Menu Options", "Order Menu Options"]

# config I think - not sure this one matters.


def run_main_sequence():
    cnfg.print_line_break()
    cnfg.print_options(main_menu)
    navigate_main_menu()

# main for now, however all navigation could be refactored into 1 navigation function from config


def navigate_main_menu():
    user_input = input('''
Please pick from the following options below using the index number shown \n 
Enter option index here: 
    ''')
    if user_input == "0":
        print("\n Bye Falicia! \n")
        return
    elif user_input == "1":
        pm.run_product_sequence()
        run_main_sequence()
    elif user_input == "2":
        cm.run_courier_sequence()
        run_main_sequence()
    elif user_input == "3":
        om.run_order_sequence()
        run_main_sequence()
    else:
        print("please pick a valid option... try to use digits only")
        run_main_sequence()


run_main_sequence()

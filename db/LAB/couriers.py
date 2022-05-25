from utils import print_with_index
import sql_read_write as sql
import pprint
import inputs as take


def get_courier_request():
    print()
    print("Courier menu options:")
    print("  0: Return to main menu")
    print("  1: Display couriers")
    print("  2: Create new courier")
    print("  3: Update existing courier")
    print("  4: Delete existing courier")
    print()
    courier_request = input("Select option (0, 1, 2, 3, 4): ")
    return courier_request


def create_new_courier():
    c_name = take.name_not_null(input("Courier name: "))
    c_phone = take.phone_number(input("Courier phone: "))
    sql.insert_new_courier((c_name, c_phone))

#########################################################


def update_existing_courier():
    couriers = sql.print_couriers()

    courier_index = take.valid_index(couriers,
                                     input("\nEnter the INDEX of the courier you would like to update: "))

    courier_name = take.name(input(
        "Hit [Enter] to skip, or provide new courier name: "))
    if courier_name == '':
        courier_name = couriers[courier_index]['courier_name']

    courier_phone = take.phone_number(input(
        "Hit [Enter] to skip, or provide new phone number: "))
    if courier_phone == '':
        courier_phone = couriers[courier_index]['courier_phone']

    courier_id = couriers[courier_index]['courier_id']
    values = courier_name, courier_phone, courier_id
    sql.update_courier_rec(values)
#########################################################


def delete_existing_courier():
    couriers = sql.print_couriers()
    courier_index = take.valid_index(couriers, input(
        "\nEnter the INDEX of the courier you would like to delete: "))
    sql.delete_courier_rec(couriers[int(courier_index)]['courier_id'])


def courier_menu():
    courier_request = None
    while courier_request != "0":
        courier_request = get_courier_request()
        if courier_request == "0":
            return
        elif courier_request == "1":
            sql.print_couriers()
        elif courier_request == "2":
            create_new_courier()
        elif courier_request == "3":
            update_existing_courier()
        elif courier_request == "4":
            delete_existing_courier()
        else:
            print("Invalid option")

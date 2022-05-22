from utils import print_with_index
import sql_read_write as sql
import pprint


def _get_courier_request():
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


def _create_new_courier(couriers):
    courier = {}
    courier['courier_name'] = c_name = input("Courier name: ")
    courier['courier_phone'] = c_phone = input("Courier phone: ")
    couriers.append(courier)
    sql.insert_new_courier((c_name, c_phone))
    return couriers


def _update_existing_courier(couriers):
    print_with_index(couriers)
    courier_index = int(input("Courier index: "))
    courier_name = input("Courier name: ")
    couriers[courier_index] = courier_name
    return couriers


def _delete_existing_courier(couriers):
    print_with_index(couriers)
    courier_index = int(input("Courier index: "))
    couriers.pop(courier_index)
    return couriers


def courier_menu(couriers):
    courier_request = None
    while courier_request != "0":
        courier_request = _get_courier_request()
        if courier_request == "0":
            return couriers
        elif courier_request == "1":
            for courier in couriers:
                print(list(courier.values())[:2])
        elif courier_request == "2":
            couriers = _create_new_courier(couriers)
        elif courier_request == "3":
            couriers = _update_existing_courier(couriers)
        elif courier_request == "4":
            couriers = _delete_existing_courier(couriers)
        else:
            print("Invalid option")

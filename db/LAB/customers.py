from utils import print_with_index
import sql_read_write as sql
import inputs as take


def get_customer_request():
    print()
    print("customer menu options:")
    print("  0: Return to main menu")
    print("  1: Display customers")
    print("  2: Create new customer")
    print("  3: Update existing customer")
    print("  4: Delete existing customer")
    print()
    customer_request = input("Select option (0, 1, 2, 3, 4): ")
    return customer_request


def create_new_customer():
    f_name = take.name_not_null(input("Customer's first name: "))
    l_name = take.name_not_null(input("Last name: "))
    flo_address = take.name_not_null(input("First line of address: "))
    postcode = take.postcode(input("Postcode: ")).upper()
    cust_phone = take.phone_number(input("Customer phone number: "))
    values = f_name, l_name, flo_address, postcode, cust_phone
    # inserts into table and returns cust_id
    cust_id = sql.insert_new_customer(values)
    return cust_id

#########################################################


def update_existing_customer(customer_index):  # Learn update commands
    customers = sql.get_customers_dict()
    #    values = f_name, l_name, flo_address, postcode, cust_phone

    f_name = take.name(input(
        "\n[Hit [Enter] to skip] Update first name: "))
    if f_name == '':
        f_name = customers[customer_index]['f_name']

    l_name = take.name(input(
        "[Hit [Enter] to skip] Update last name: "))
    if l_name == '':
        l_name = customers[customer_index]['l_name']

    flo_address = take.name(input(
        "[Hit [Enter] to skip] Update the first line of address: "))
    if flo_address == '':
        flo_address = customers[customer_index]['flo_address']

    postcode = take.postcode(input(
        "[Hit [Enter] to skip] Update postcode: "))
    if postcode == '':
        postcode = customers[customer_index]['postcode']

    cust_phone = take.phone_number(input(
        "[Hit [Enter] to skip] Update phone number: "))
    if cust_phone == '':
        cust_phone = customers[customer_index]['cust_phone']

    cust_id = customers[customer_index]['cust_id']
    values = f_name, l_name, flo_address, postcode, cust_phone, cust_id
    sql.update_customer_rec(values)

#######################################################


def delete_existing_customer():
    customers = sql.print_customers()
    customer_index = take.valid_index(customers, input(
        "\n INDEX of the customer you would like to delete: "))
    sql.delete_customer_rec(customers[int(customer_index)]['cust_id'])


def new_or_existing_cust():
    new_existing = input(
        "Are you creating an order for a new [0] or existing [1] customer? ")
    if new_existing == '0':
        # take customer details, create a new customer, retreive cust ID
        cust_id = create_new_customer()
        return cust_id
    if new_existing == '1':
        # select from list of customers
        customers = sql.print_customers()
        inx = take.valid_index(customers, input("customer INDEX: "))
        cust_id = customers[int(inx)]['cust_id']
        return cust_id
    else:
        print("\nInvalid selection. \n")
        new_or_existing_cust()


def customer_menu():
    customer_request = None
    while customer_request != "0":
        customer_request = get_customer_request()
        if customer_request == "0":
            return
        elif customer_request == "1":
            sql.print_customers()
        elif customer_request == "2":
            create_new_customer()
        elif customer_request == "3":
            customers = sql.print_customers()
            customer_index = int(
                input("INDEX of the customer you would like to update: "))
            update_existing_customer(customer_index)
        elif customer_request == "4":
            delete_existing_customer()
        else:
            print("Invalid option")

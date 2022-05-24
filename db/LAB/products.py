from utils import print_with_index
import sql_read_write as sql
import inputs as take


def get_product_request():
    print()
    print("Product menu options:")
    print("  0: Return to main menu")
    print("  1: Display products")
    print("  2: Create new product")
    print("  3: Update existing product")
    print("  4: Delete existing product")
    print()
    product_request = input("Select option (0, 1, 2, 3, 4): ")
    return product_request


def create_new_product():
    p_name = take.product_name()
    p_price = take.product_price()
    sql.insert_new_product((p_name, p_price))

#########################################################


def update_existing_product():  # Learn update commands
    products = sql.print_products()

    product_index = int(
        input("INDEX of the product you would like to update: "))

    product_name = input(
        "Hit [Enter] to skip, or provide new Product name: ")
    if product_name == '':
        product_name = products[product_index]['product_name']

    price = input("Hit [Enter] to skip, or provide new Price: £")
    if price == '':
        price = products[product_index]['price']
    else:
        price = f'£{price}'

    product_id = products[product_index]['product_id']
    values = product_name, price, product_id
    sql.update_product_rec(values)

#######################################################


def delete_existing_product():
    products = sql.print_products()
    product_index = input("INDEX of the product you would like to delete: ")
    sql.delete_product_rec(products[int(product_index)]['product_id'])


def product_menu():
    product_request = None
    while product_request != "0":
        product_request = get_product_request()
        if product_request == "0":
            return
        elif product_request == "1":
            sql.print_products()
        elif product_request == "2":
            create_new_product()
        elif product_request == "3":
            update_existing_product()
        elif product_request == "4":
            delete_existing_product()
        else:
            print("Invalid option")

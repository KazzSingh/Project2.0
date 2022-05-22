from utils import print_with_index
import sql_read_write as sql


def _get_product_request():
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


def _create_new_product(products):
    product = {}
    product["product_id"] = ''
    product["product_name"] = p_name = input("product name: ")
    product["price"] = p_price = f'£{input("product price: £")}'
    product_ID = sql.insert_new_product((p_name, p_price))
    product["product_id"] = product_ID
    products.append(product)
    return products


def _update_existing_product(products):
    print_with_index(products)
    product_index = int(input("Product index: "))
    product_name = input("Product name: ")
    products[product_index] = product_name
    return products


def _delete_existing_product(products):
    print_with_index(products)
    product_index = int(input("Product index: "))
    products.pop(product_index)
    return products


def product_menu(products):
    product_request = None
    while product_request != "0":
        product_request = _get_product_request()
        if product_request == "0":
            return products
        elif product_request == "1":
            for product in products:
                print(list(product.values()))
        elif product_request == "2":
            products = _create_new_product(products)
        elif product_request == "3":
            products = _update_existing_product(products)
        elif product_request == "4":
            products = _delete_existing_product(products)
        else:
            print("Invalid option")

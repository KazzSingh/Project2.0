import read_write as rw
import pymysql
import os
from dotenv import load_dotenv
import pprint
import csv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################

# INSERTIONINGS

##################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################


################################################################################################################
# INSERT new product INTO table
################################################################################################################


def insert_new_product(values):
    cursor = connection.cursor()
    insert = ("INSERT INTO products (product_name, price) VALUES (%s, %s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Product successfully added")
    product_ID = cursor.lastrowid
    cursor.close()
    return product_ID


# ################################################################################################################
# # INSERT new courier INTO table
# ################################################################################################################


def insert_new_courier(values):
    cursor = connection.cursor()
    insert = ("INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Success")
    cursor.close()
#     connection.close()


# ################################################################################################################
# # INSERT new customer INTO table
# ################################################################################################################


# 'values' will be a tuple, in this case the tuple has 2 objects inside
def insert_new_customer(values):
    cursor = connection.cursor()
    # (%s, %s) will be replaced with the tuple I've provided. Each object in the tuple will require its own '%s'
    insert = ("INSERT INTO customers (f_name, l_name, first_line_of_address, postcode, cust_phone) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(insert, values)
    connection.commit()
    cust_id = cursor.lastrowid
    print("Success")
    cursor.close()
    return cust_id
    # connection.close()


# ################################################################################################################
# # INSERT new order INTO table
# ################################################################################################################


def insert_new_order(values):
    print(values)
    cursor = connection.cursor()
    cust_id, courier_id, basket, order_status = values
    insert = (
        "INSERT INTO orders (cust_id, courier_id, basket, order_status) VALUES (%s,%s,%s,%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    order_id = cursor.lastrowid
    print("Success")
    cursor.close()
    return order_id
#     connection.close()


##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################

# UPDATIONINGS

##################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################


################################################################################################################
# UPDATE EXISTING product INTO table
################################################################################################################


def update_product_rec(values):
    cursor = connection.cursor()
    insert = (
        "UPDATE products SET product_name = (%s), price = (%s)  WHERE product_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Updated Successfully")
    cursor.close()


# # ################################################################################################################
# # # UPDATE EXISTING courier INTO table
# # ################################################################################################################


def update_courier_rec(values):
    cursor = connection.cursor()
    insert = (
        "UPDATE couriers SET courier_name = (%s), courier_phone = (%s)  WHERE courier_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Updated Successfully")
    cursor.close()


# # ################################################################################################################
# # # UPDATE EXISTING customer INTO table
# # ################################################################################################################


def update_customer_rec(values):
    cursor = connection.cursor()
    insert = (
        "UPDATE customers SET f_name = (%s), l_name = (%s), first_line_of_address = (%s), postcode = (%s), cust_phone = (%s) WHERE cust_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Updated Successfully")
    cursor.close()


# # ################################################################################################################
# # # UPDATE EXISTING order INTO table
# # ################################################################################################################


def update_order_rec(values):
    cursor = connection.cursor()
    insert = (
        "UPDATE orders SET courier_id = (%s), basket = (%s)  WHERE order_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Updated Successfully")
    cursor.close()


# # ################################################################################################################
# # # UPDATE existing ORDER STATUS INTO table
# # ################################################################################################################


def update_order_status_rec(values):
    cursor = connection.cursor()
    insert = (
        "UPDATE orders SET order_status = (%s)  WHERE order_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("Updated Successfully")
    cursor.close()
##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################

# DELETIONINGS

##################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################


################################################################################################################
# DELETE EXISTING product FROM table
################################################################################################################


def delete_product_rec(values):
    cursor = connection.cursor()
    insert = ("DELETE FROM products WHERE product_id=(%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("\n Record deleted \n")
    cursor.close()


# # ################################################################################################################
# # # DELETE EXISTING courier INTO table
# # ################################################################################################################


def delete_courier_rec(values):
    cursor = connection.cursor()
    insert = (
        "DELETE FROM couriers WHERE courier_id = (%s)")
    # Execute SQL query
    try:
        cursor.execute(insert, values)
        print("\n Record deleted \n")
    except pymysql.err.IntegrityError:
        print("\nCourier has active orders to complete. Please reallocate the order from the orders before trying again.")
    connection.commit()
    cursor.close()


# # ################################################################################################################
# # # DELETE EXISTING customer FROM table
# # ################################################################################################################


def delete_customer_rec(values):
    cursor = connection.cursor()
    insert = (
        "DELETE FROM customers WHERE cust_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("\n Record deleted \n")
    cursor.close()


# # ################################################################################################################
# # # DELETE EXISTING order FROM table
# # ################################################################################################################


def delete_order_rec(values):
    cursor = connection.cursor()
    insert = (
        "DELETE FROM orders WHERE order_id = (%s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    print("\n Record deleted \n")
    cursor.close()


##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################

# RETRIEVE DATA IN DICT FORM
# PRINT DICTS
# PRINT SPECIFIC RECORDS

##################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################

def print_products():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    fieldnames = ['product_id', 'product_name', 'price']
    rows = cursor.fetchall()
    products = []
    # [item for item in rows]
    for row in rows:
        products.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    print("{:<8} {:<15} {:<15} {:<20}".format(
        'Index', 'product_id', 'product_name', 'price'))
    for i, product in enumerate(products):
        product_id, name, price = product.values()
        print("{:<8} {:<15} {:<15} {:<10}".format(i, product_id, name, price))
    return products


def print_couriers():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    fieldnames = ['courier_id', 'courier_name', 'courier_phone']
    rows = cursor.fetchall()
    couriers = []
    for row in rows:
        couriers.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    print("{:<8} {:<15} {:<15} {:<20}".format(
        'Index', 'courier_id', 'courier_name', 'courier_phone'))
    for i, courier in enumerate(couriers):
        courier_id, courier_name, courier_phone = courier.values()
        print("{:<8} {:<15} {:<15} {:<10}".format(
            i, courier_id, courier_name, courier_phone))
    return couriers


def print_specific_courier(courier_id):
    cursor = connection.cursor()
    command = ("SELECT * FROM couriers WHERE courier_id=(%s)")
    cursor.execute(command, courier_id)
    fieldnames = ['courier_id', 'courier_name', 'courier_phone']
    rows = cursor.fetchall()
    couriers = []
    for row in rows:
        couriers.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    print("{:<15} {:<15} {:<20}".format(
        'courier_id', 'courier_name', 'courier_phone'))
    for courier in couriers:
        courier_id, courier_name, courier_phone = courier.values()
        print("{:<15} {:<15} {:<10}".format(
            courier_id, courier_name, courier_phone))
    return couriers


def print_customers():
    customers = get_customers_dict()
    print("\n")
    print("{:<8} {:<9} {:<9} {:<9} {:<23} {:<10} {:<15}".format(
        'Index', 'cust_id', 'f_name', 'l_name',
        'flo_address', 'postcode', 'cust_phone'))
    for i, customer in enumerate(customers):
        cust_id, f_name, l_name, flo_address, postcode, cust_phone = customer.values()
        print("{:<8} {:<9} {:<9} {:<9} {:<23} {:<10} {:<15}".format(i, cust_id, f_name, l_name,
                                                                    flo_address, postcode, cust_phone))
    return customers


def print_specific_customer(cust_id):
    cursor = connection.cursor()
    command = ("SELECT * FROM customers WHERE cust_id=(%s)")
    cursor.execute(command, cust_id)
    fieldnames = ['cust_id', 'f_name', 'l_name',
                  'flo_address', 'postcode', 'cust_phone']
    rows = cursor.fetchall()
    customers = []
    for row in rows:
        customers.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    print()
    print("{:<9} {:<9} {:<9} {:<23} {:<10} {:<15}".format(
        'cust_id', 'f_name', 'l_name',
        'flo_address', 'postcode', 'cust_phone'))
    for customer in customers:
        cust_id, f_name, l_name, flo_address, postcode, cust_phone = customer.values()
        print("{:<9} {:<9} {:<9} {:<23} {:<10} {:<15}".format(
            cust_id, f_name, l_name, flo_address, postcode, cust_phone))
    return customer


def get_customers_dict():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    fieldnames = ['cust_id', 'f_name', 'l_name',
                  'flo_address', 'postcode', 'cust_phone']
    rows = cursor.fetchall()
    customers = []
    for row in rows:
        customers.append(dict(zip(fieldnames, row)))
    cursor.close()
    return customers


def print_orders():
    orders = get_orders_dict()
    print("{:<8} {:<10} {:<10} {:<10} {:<20} {:<10}".format(
        'Index', 'order_id', 'cust_id', 'courier', 'basket', 'status'))
    for i, order in enumerate(orders):
        order_id, cust_id, courier, basket, status = order.values()
        print("{:<8} {:<10} {:<10} {:<10} {:<20} {:<10}".format(
            i, order_id, cust_id, courier, basket, status))
    return orders


def get_orders_dict():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    fieldnames = ['order_id', 'cust_id', 'courier_id', 'basket', 'status']
    rows = cursor.fetchall()
    orders = []
    for row in rows:
        orders.append(dict(zip(fieldnames, row)))
    cursor.close()
    return orders


# def load_data():
#     products = load_products()
#     couriers = load_couriers()
#     customers = load_customers()
#     orders, order_status_options = load_orders()
#     return products, couriers, customers, orders, order_status_options

################################################################################################################
# RETRIEVE FROM DB
################################################################################################################

################################################################################################################

################################################################################################################
# SAVE DATA #
#################################################################################################################


def save_data(products, couriers, orders):
    with open("products.csv", 'w', newline='') as f:
        fieldnames = ['product_id', 'product_name', 'price']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in products:
            writer.writerow(row)

    with open("couriers.csv", 'w', newline='') as f:
        fieldnames = ['courier_ID', 'courier_name', 'courier_phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in couriers:
            writer.writerow(row)

    with open("customers.csv", 'w', newline='') as f:
        fieldnames = ['cust_id', 'f_name', 'l_name', 'flo_address', 'postcode',
                      'cust_phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in orders:
            writer.writerow(row)

    with open("orders.csv", 'w', newline='') as f:
        fieldnames = ['cust_id', 'courier', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in orders:
            writer.writerow(row)


################################################################################################################
#  NOTES - TO DO
################################################################################################################

#

########################################################################################################

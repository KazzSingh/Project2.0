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

products, couriers, orders, order_status_options = rw.load_data()

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
    print("done")
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
    print("done")
    cursor.close()
    return cust_id
    # connection.close()


# ################################################################################################################
# # INSERT new order INTO table
# ################################################################################################################


def insert_new_order(values):
    cursor = connection.cursor()
    insert = ("INSERT INTO order (cust_id, courier_id) VALUES (%s, %s)")
    # Execute SQL query
    cursor.execute(insert, values)
    connection.commit()
    order_id = cursor.lastrowid
    print("done")
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


# def insert_new_product(values):
#     cursor = connection.cursor()
#     insert = ("INSERT INTO products (product_name, price) VALUES (%s, %s)")
#     # Execute SQL query
#     cursor.execute(insert, values)
#     connection.commit()
#     print("done")
#     cursor.close()


# # ################################################################################################################
# # # UPDATE EXISTING courier INTO table
# # ################################################################################################################


# def insert_new_courier(values):
#     cursor = connection.cursor()
#     insert = ("INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)")
#     # Execute SQL query
#     cursor.execute(insert, values)
#     connection.commit()
#     print("done")
#     cursor.close()


# # ################################################################################################################
# # # UPDATE EXISTING customer INTO table
# # ################################################################################################################


# # #
# def insert_new_customer(values):
#     cursor = connection.cursor()
#     insert = ("INSERT INTO customers (f_name, l_name, first_line_of_address, postcode, cust_phone) VALUES (%s, %s)")
#     cursor.execute(insert, values)
#     connection.commit()
#     print("done")
#     cust_id = cursor.lastrowid
#     cursor.close()
#     return cust_id


# # ################################################################################################################
# # # UPDATE EXISTING order INTO table
# # ################################################################################################################


# def insert_new_courier(values):
#     cursor = connection.cursor()
#     insert = ("INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)")
#     # Execute SQL query
#     cursor.execute(insert, values)
#     connection.commit()
#     print("done")
#     cursor.close()


##################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################

# RETRIEVE INFO
# INSERT WHOLE LIST
# CREATE TABLE

##################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################

def _load_products():
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

    return products


def _load_couriers():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM couriers")
    fieldnames = ['courier_ID', 'courier_name', 'courier_phone']
    rows = cursor.fetchall()
    couriers = []
    for row in rows:
        couriers.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    return couriers


def _load_customers():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    fieldnames = ['cust_id', 'f_name', 'l_name',
                  'flo_address', 'postcode', 'cust_phone']
    rows = cursor.fetchall()
    customers = []
    for row in rows:
        customers.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    return customers


def _load_orders():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    fieldnames = ['order_id', 'cust_id', 'courier', 'status']
    rows = cursor.fetchall()
    orders = []
    for row in rows:
        orders.append(dict(zip(fieldnames, row)))
    cursor.close()
    # connection.close() DO NOT CLOSE THE CONNECTION
    order_status_options = ["preparing", "sent", "cancelled"]
    return orders, order_status_options


def load_data():
    products = _load_products()
    couriers = _load_couriers()
    customers = _load_customers()
    orders, order_status_options = _load_orders()
    return products, couriers, customers, orders, order_status_options

################################################################################################################
# RETRIEVE FROM DB
################################################################################################################
# Gets all rows from the result
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM customers")
# fieldnames = ['cust_id', 'f_name', 'l_name',
#               'flo_address', 'postcode', 'cust_phone']
# rows = cursor.fetchall()
# customers = []
# for row in rows:
#     customers.append(dict(zip(fieldnames, row)))
# return customers

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:

#         break
# #     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')


# # # Closes the cursor so will be unusable from this point
# cursor.close()

# # # Closes the connection to the DB, make sure you ALWAYS do this
# connection.close()

################################################################################################################
# INSERT whole list INTO table
################################################################################################################
# cursor = connection.cursor()

# insert = ("INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)")
# val = []
# for courier in couriers:
#     val.append((courier['courier_name'], courier['courier_phone']))
#     print((courier['courier_name'], courier['courier_phone']))
# # Execute SQL query
# cursor.executemany(insert, val)
# connection.commit()
# print("done")
# # Closes the cursor so will be unusable from this point
# cursor.close()

# # Closes the connection to the DB, make sure you ALWAYS do this
# connection.close()

#


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

# WE NOW HAVE A PRODUCTS/COURIERS/CUSTOMERS/ORDERS TABLE


# CREATING A PRODUCT OR COURIER IS FINE:

# CREATING AN ORDER WILL BE SLIGHTLY DIFFERENT
############################################## CREATE NEW ORDER #################################################
# NEW OR EXISTING CUSTOMER?
#   EXISTING:
# DO YOU KNOW THE CUSTOMER ID NUMBER? no?
# ASK FOR THE FIRST NAME, SECOND NAME, and POSTCODE
# THIS WILL BE CHECKED IN THE DATABASE FOR MATCHES,
# SHOULD THERE BE ONLY 1 MATCH, THE USER SHALL BE NOTIFIED "RECORD EXISTS" WITH LIST OF MATCHING RECORDS
# IF NO MATCH FOUND, USER WILL BE NOTIFIED AND APP WILL CONTINUE TO CREATE NEW CUSTOMER, PROMPTED FOR FIRST LINE OF ADDRESS AND PHONE NUMBER
#   NEW:
# FIRST NAME, SECOND NAME, FIRST LINE OF ADDRESS, POSTCODE, PHONE NUMBER
# UPDATE customers TABLE sql
# RETRIEVE cust_id, STORE IN VARIABLE AND CONTINUE WITH ORDER DETAILS
# WHAT PRODUCTS WOULD YOU LIKE TO ORDER? (NO QUANTITIES, YET.)
# WHICH COURIER WOULD YOU LIKE TO CHOOSE? (NOTHING TO DEFFERENCIATE, YET?)


# BEFORE WORKING ON CREATING AN ORDER:
# START WORKING ON 'UPDATING'AND DELETION RECORDS IN THE DATABASE

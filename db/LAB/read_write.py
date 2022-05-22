import csv


def _load_products():
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        products = list(reader)
    return products


def _load_couriers():
    with open("couriers.csv", "r") as f:
        reader = csv.DictReader(f)
        couriers = list(reader)
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
    connection.close()
    return customers


def _load_orders():
    with open("orders.csv") as f:
        reader = csv.DictReader(f)
        orders = list(reader)
    order_status_options = ["preparing", "sent", "cancelled"]
    return orders, order_status_options


def load_data():
    products = _load_products()
    couriers = _load_couriers()
    orders, order_status_options = _load_orders()
    return products, couriers, orders, order_status_options


def save_data(products, couriers, orders):
    with open("products.csv", 'w', newline='') as f:
        fieldnames = ['product_name', 'price']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in products:
            writer.writerow(row)

    with open("couriers.csv", 'w', newline='') as f:
        fieldnames = ['courier_name', 'courier_phone']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in couriers:
            writer.writerow(row)

    with open("orders.csv", 'w', newline='') as f:
        fieldnames = ['customer_name', 'customer_address',
                      'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for row in orders:
            writer.writerow(row)

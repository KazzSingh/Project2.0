def save_csv_data(list, file_name):
    dict_data = f"source/data/{file_name}"
    with open(dict_data, mode="w") as data:
        if file_name == "couriers.csv":
            key_headers = ["name", "number"]
        elif file_name == "products.csv":
            key_headers = ["name", "price"]
        elif file_name == "orders.csv":
            key_headers = ["customer_name", "customer_address",
                           "customer_phone", "courier", "status", "items"]
        writer = DictWriter(data, fieldnames=key_headers)
        writer.writeheader()
        for num in range(len(list)):
            writer.writerow(list[num])


def load_csv_data(file_name):
    data_path = f"source/data/{file_name}"
    with open(data_path, "r") as data:
        list = DictReader(data)
        if file_name == "products.csv":
            for row in list:
                products.products_list.append(row)
        elif file_name == "couriers.csv":
            for row in list:
                couriers.couriers_list.append(row)
        elif file_name ==

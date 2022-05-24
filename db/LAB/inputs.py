def product_name():
    p_name = input("Enter the name of the product you would like to add: ")
    return p_name.title()


def product_price():
    try:
        p_price = "{:.2f}".format(
            float(input("Enter the price of the product [£0.00]: £")))
    except ValueError:
        print("Please enter a number only in the following format [0.00]")
        take_product_price()
    return f"£{p_price}"


take_product_price()

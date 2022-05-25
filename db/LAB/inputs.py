import sql_read_write as sql
import pprint


def valid_index(_list, index):
    try:
        _list[int(index)]
        return int(index)
    except ValueError:
        print("\nInvalid index. Please enter a number using digits only.")
        return valid_index(_list, input("Please try again:-  "))
    except IndexError:
        print("\nInvalid Index. Please choose from the options available.")
        return valid_index(_list, input("Please try again:-  "))


def name(n):
    if n == '':
        return n
    if not n.isdigit():
        if len(n) < 2:
            print("Name must be at least 2 characters long.")
            return name(input("Please try again:-  "))
        if len(n) > 21:
            print("Name must be less than 22 characters long.")
            return name(input("Please try again:-  "))
    else:
        print("Name must use alphabetical characters only.")
        return name(input("Please try again:-  "))

    return n.title()


def name_not_null(n):
    if not n.isdigit():
        if len(n) < 2:
            print("Name must be at least 2 characters long.")
            return name_not_null(input("Please try again:-  "))
        if len(n) > 21:
            print("Name must be less than 22 characters long.")
            return name_not_null(input("Please try again:-  "))
    else:
        print("Name must use alphabetical characters only.")
        return name_not_null(input("Please try again:- "))

    return n.title()


def price(p):
    if p == '':
        return p
    try:
        p = "{:.2f}".format(float(p))
        return f"£{p}"
    except ValueError:
        print("Please enter a number only in the following format [0.00]")
        return take_product_price(p)


def phone_number(number):
    if number == '':
        return number
    if not number.isdigit():
        print("Invalid phone number. Must be a number; 6-12 digits long. ")
        return phone_number(input("Please try again:-  "))
    if len(number) < 6:
        print("Invalid phone number. Number too short.")
        return phone_number(input("Please try again:-  "))
    if len(number) > 12:
        print("Invalid phone number. Number too long.")
        return phone_number(input("Please try again:-  "))
    return number


def postcode(pc):
    if pc == '':
        return pc
    if len(pc) < 5:
        print("postcode must be at least 5 characters long.")
        return postcode(input("Please try again:-  ").upper())
    if len(pc) > 8:
        print("postcode must be less than 7 characters long.")
        return postcode(input("Please try again:-  ").upper())
    return pc

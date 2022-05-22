
# config
def print_options(options_list):
    for i, option in enumerate(options_list):
        print(i, option)


# ##########################################################################################

def confirm_choice(choice, currency_symbol=""):
    confirm = input(
        f"\n{currency_symbol}{choice}? Are you sure? enter [1] for yes, [any other key] for no: ")
    if confirm == "1":
        return True
    else:
        return False

# ###########################################################################################


def print_line_break():
    print("\n#######################################################################################\n")


# ###########################################################################################

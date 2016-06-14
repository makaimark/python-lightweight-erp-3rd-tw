# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()

table = data_manager.get_table_from_file(current_file_path + "/customers.csv")

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#


def start_module():
    options = ["1. Show items",
               "2. Add items",
               "3. Remove items",
               "4. Update items",
               "5. Get longest name id",
               "6. Get subscribed emails",
               "0. Back to the main menu"]

    while True:
        # print(options)
        ui.print_menu(list_options, exit_message, options)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        # inputs = input("Please enter a number:")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/customers.csv")

        if option == "1":
            show_table()
        elif option == "2":
            add()
        elif option == "3":
            remove()
        elif option == "4":
            update()
        elif option == "5":
            get_longest_name_id()
        elif option == "6":
            get_subscribed_emails()
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "name", "e-mail", "subscribed"]
    table = data_manager.get_table_from_file(current_file_path + "/customers.csv")
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    # title_list = ["ID", "name", "e-mail", "subscribed"]

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # title_list = ["ID"]

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # title_list = ["ID", "name", "e-mail", "subscribed"]

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    # title_list = ["ID"]

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # title_list = ["ID", "name", "e-mail", "subscribed"]

    pass

start_module()

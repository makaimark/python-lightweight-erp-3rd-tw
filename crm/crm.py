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


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "name", "e-mail", "subscribed"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["name", "e-mail", "subscribed"]
    common.common_add(table, title_list)
    ui.print_table(table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table):
    list_labels = ["ID"]
    id_ = ui.get_inputs(list_labels, "")
    common.common_remove(table, id_[0])
    ui.print_table(table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table):
    title_list = ["name", "e-mail", "subscribed"]
    id_ = ui.get_inputs(["ID:"], "")
    common.common_update(table, title_list, id_[0])
    ui.print_table(table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    longest_names = [' ']
    longest = 0
    result = ""
    for line in table:
        if len(line[1]) > longest:
            longest_names = []
            longest_names.append(line[0])
            longest = len(line[1])
        elif len(line[1]) == longest:
            longest_names.append(line[0])
            longest = len(line[1])
    ui.print_result(longest_names, ' ')
    ui.print_result(longest_names)
    return longest_names
    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    data_line = table
    subscribed = []
    for i in data_line:
        if i[3] == "1":
            subscribed.append("{0};{1}".format(i[2], i[1]))
    ui.print_result(subscribed)
    return subscribed
    # pass


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

    table = data_manager.get_table_from_file(current_file_path + "/customers.csv")

    while True:
        id_ = []
        ui.print_menu("", options, "Error message")
        option = ui.get_inputs(["Please enter a number: "], "")

        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            table = remove(table)
        elif option[0] == "4":
            table = update(table)
        elif option[0] == "5":
            get_longest_name_id(table)
        elif option[0] == "6":
            title_list = ["email", "name"]
            subscribed_email = get_subscribed_emails(table)
            sub_list = []
            for i in range(len(subscribed_email)):
                sub_list.append(subscribed_email[i].split(";"))
            ui.print_table(sub_list, title_list)
        elif option[0] == "0":
            break
        else:
            raise KeyError("There is no such option.")
            pass
        data_manager.write_table_to_file(current_file_path + "/customers.csv", table)

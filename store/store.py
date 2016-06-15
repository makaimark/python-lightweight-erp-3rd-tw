# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    options = ["1. Show items",
    "2. Add items",
    "3. Remove items",
    "4. Update items",
    "5. Get counts by manufacturers",
    "6. Get average by manufacturer",
    "0. Back to the main menu"]

    table = data_manager.get_table_from_file(current_file_path + "/games.csv")
    while True:
        ui.print_menu("", options, "Error message")
        option = ui.get_inputs(["Please enter a number: "], "")

        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            table = add(table)
        elif option[0] == "3":
            table = remove(table)
        elif option[0] == "4":
            update(table)
        elif option[0] == "5":
            get_counts_by_manufacturers(table)
        elif option[0] == "6":
            get_average_by_manufacturer(table)
        elif option[0] == "0":
            break
        else:
            raise KeyError("There is no such option.")
            pass
        data_manager.write_table_to_file(current_file_path + "/games.csv", table)

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Title", "Manufacturer", "Price", "In stock"]
    ui.print_table(table, title_list)
    # your code
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Title", "Manufacturer", "Price", "In stock:"]
    table = common.common_add(table, title_list)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table):
    list_labels = ["ID"]
    id_ = ui.get_inputs(list_labels, "")
    table = common.common_remove(table, id_[0])
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table):
    title_list = ["Title", "Manufacturer", "Price", "In stock:"]
    id_ = ui.get_inputs(["ID:"], "")
    common.common_update(table, title_list, id_[0])
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    data = {}
    for i in range(len(table)):
        stat = table[i][2] in data
        if stat is not True:
            data[table[i][2]] = 1
        else:
            data[table[i][2]] += 1
    # ui.print_table(data, ' ')
    print(data)  # works with print


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table):
    counter = 0
    summa = 0
    for i in range(len(table)):
        if manufacturer == table[i][2]:
            summa += int(table[i][4])
            counter += 1
    result = summa/counter
    # print_table(res, "Average by Manufacturer:")
    print(result)

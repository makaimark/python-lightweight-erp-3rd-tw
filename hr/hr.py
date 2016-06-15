# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
                "5. Get oldest person",
                "6. Get closest person to average",
                "0. Back to the main menu"]

    table = data_manager.get_table_from_file(current_file_path + "/persons.csv")
    while True:
        ui.print_menu("", options, "Error message")
        option = ui.get_inputs(["Please enter a number: "], "")

        if option[0] == "1":
            show_table(table)
        elif option[0] == "2":
            add(table)
        elif option[0] == "3":
            remove(table)
        elif option[0] == "4":
            update(table)
        elif option[0] == "5":
            get_oldest_person(table)
        elif option[0] == "6":
            get_persons_closest_to_average(table)
        elif option[0] == "0":
            break
        else:
            raise KeyError("There is no such option.")
            pass
        data_manager.write_table_to_file(current_file_path + "/persons.csv", table)

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "name", "birthdate"]
    ui.print_table(table, title_list)

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["name", "birthdate"]
    table = common.common_add(table, title_list)
    ui.print_table(table, title_list)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table):
    list_labels = ["ID"]
    id_ = ui.get_inputs(list_labels, "")
    table = common.common_remove(table, id_[0])
    ui.print_table(table, title_list)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table):
    title_list = ["name", "birthdate"]
    id_ = ui.get_inputs(["ID:"], "")
    common.common_update(table, title_list, id_[0])
    ui.print_table(table, title_list)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    years = []
    persons = []
    title_list = "Oldest persons"
    for line in table:
        years.append(int(line[2]))
    for line in table:
        if int(line[2]) <= min(years):
            persons.append(line[1])
    ui.print_result(persons, "")
    return persons




# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    label = "Closest person to average"
    average_age = 0
    b = 1000
    age_list = []
    avg_diff = 0
    result = []
    for line in table:
        data = [line[1], int(line[2]), avg_diff]
        age_list.append(data)
    for line in table:
        average_age += int(line[2])
    average_age = int(average_age / len(age_list))
    for line in age_list:
        line[2] = abs(average_age - line[1])
        if line[2] < b:
            b = line[2]
    for line in age_list:
        if line[2] == b:
            result.append(line[0])
    ui.print_result(" ,".join(result), label)
    return result

# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)

import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()

table = data_manager.get_table_from_file(current_file_path + "/items.csv")


def show_table(table):
    title_list = ["ID", "month", "day", "year", 'type', 'amount']
    ui.print_table(table, title_list)
    return table
    pass


def add(table):
    title_list = ["month", "day", "year", 'type', 'amount']
    table = common.common_add(table, title_list)

    return table


def remove(table):
    list_labels = ["ID"]
    id_ = ui.get_inputs(list_labels, "")
    table = common.common_remove(table, id_[0])

    return table


def update(table):

    title_list = ["month", "day", "year", 'type', 'amount']
    id_ = ui.get_inputs(["ID:"], "")
    common.common_update(table, title_list, id_[0])

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    max_value = 0
    max_key = ""
    profit_year = {}

    for i in table:
        if i[3] not in profit_year.keys():
            if i[4] == "in":
                profit_year[i[3]] = int(i[5])
            elif i[4] == "out":
                profit_year[i[3]] = int(i[5])
        if i[3] in profit_year.keys():
            if i[4] == "in":
                profit_year[i[3]] += int(i[5])
            elif i[4] == "out":
                profit_year[i[3]] -= int(i[5])

    for k in profit_year:
        if profit_year[k] > max_value:
            max_value = profit_year[k]
            max_key = k
    return k

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass


def start_module():
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update table",
               "Year with most profit",
               "Average profit in a given year"]

    table = data_manager.get_table_from_file(current_file_path + "/items.csv")
    result_year_max = 0

    while True:
        ui.print_menu("Accounting menu", options, 'Back to main menu')
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
            result_year_max = which_year_max(table)
        elif option[0] == "6":
            avg_amount(table, year)
        elif option[0] == "0":
            break
        else:
            raise KeyError("There is no such option.")
            pass
        data_manager.write_table_to_file(current_file_path + "/items.csv", table)

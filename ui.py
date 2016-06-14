table = [["kH34Ju", "Age of Empires II: The Age of Kings", "Ensemble Studios", "32", "32"],
["jH34Ju", "Age of Mythology", "Ensemble Studios", "40", "4"],
["tH34Ju", "Age of Empires II: The Conquerors", "Ensemble Studios", "30", "3"]]

title_list = ["id", "name", "kiado", "randomnum1", "random1"]


# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    max_len_list = 0
    max_len_element = [0, 0, 0, 0, 0, 0]
    counter = 0
    formatted_string = ""
    for i in table:
        counter = 0
        for j in i:
            if len(j) > max_len_element[counter] or max_len_element[counter] < len(title_list[counter]):
                if len(j) > len(title_list[counter]):
                    max_len_element[counter] = len(j)
                else:
                    max_len_element[counter] = len(title_list[counter])
                counter += 1

    max_len_list = sum(max_len_element) + 16    # 10 | and 10 spaces

    counter = 0
    print("-" * max_len_list)

    for i in title_list:
        if counter == 4:
            formatted_string = formatted_string + ("| {:^%d} |" % max_len_element[counter]).format(i)
        else:
            formatted_string = formatted_string + ("| {:^%d} " % max_len_element[counter]).format(i)
        counter += 1
    print(formatted_string)
    print("-" * max_len_list)

    formatted_string = ""
    for i in table:
        counter = 0
        for j in i:
            if counter == 4:
                formatted_string = formatted_string + ("| {:^%d} |" % max_len_element[counter]).format(j)
            else:
                formatted_string = formatted_string + ("| {:^%d} " % max_len_element[counter]).format(j)
            counter += 1
        print(formatted_string)
        print("-" * max_len_list)
        formatted_string = ""

    pass

print_table(table, title_list)


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    if result is list:
        print(label + ":" + result)

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):

    counter = 0
    print(title)
    for i in list_options:
        print("("+counter+")" + i)
        counter += 1
    print("(0)" + exit_message)

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []

    inputs = input(list_labels)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print(message)

    pass

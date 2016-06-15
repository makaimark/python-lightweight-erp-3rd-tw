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
    max_len_element = [0 for i in range(len(title_list))]
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

    max_len_list = sum(max_len_element) + 16    # 6 | and 10 spaces

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


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    if isinstance(result, str):
        print(label)
        print("\t" + result)
    elif isinstance(result, dict):
        print(label)
        for i in result:
            print("\t" + "-" + i + " --> " + result[i])
    elif isinstance(result, list):
        print(label)
        for i in range(len(result)):
            print("\t" + "-" + result[i])
    else:
        print(label)
        print("\t" + str(result))

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

    counter = 1
    print(title)
    for i in list_options:
        print("("+str(counter)+")" + "\t" + str(i))
        counter += 1
    print("(0)" + "\t" + exit_message)

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for i in list_labels:
        inputs.append(input(i + " "))

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print(message)

    pass

from logic import *


def printmenu():
    # Displays the menu
    msg = "Menu:\n"
    msg += "\t 1 View the list\n"
    msg += "\t 2 Add a nr to the end of the list\n"
    msg += "\t 3 Insert a number in the list\n"
    msg += "\t 4 Remove a number by index\n"
    msg += "\t 5 Replace all old values with new ones\n"
    msg += "\t 6 Prime numbers between two index\n"
    msg += "\t 7 Odd numbers between two index\n"
    msg += "\t 8 Sum of numbers between two index\n"
    msg += "\t 9 Gcd of numbers between two index\n"
    msg += "\t 10 Max of numbers between two index\n"
    msg += "\t 11 Filter prime numbers\n"
    msg += "\t 12 Filter negative numbers\n"
    msg += "\t 13 Undo\n"
    msg += "\t 0 Exit\n"
    print(msg)


def main():
    # Starts the app
    my_list = [1, 2, 3, 54, 33, 13, 22, 901, 21, 14]
    stop = False
    while stop == False:
        printmenu()
        option = int(input("Enter option:"))
        if option == 1:
            print(my_list)
        elif option == 2:
            q = my_list[:]
            nr = int(input("Nr:"))
            add(my_list, nr)
        elif option == 3:
            q = my_list[:]
            nr = int(input("Nr:"))
            index = int(input("Index:"))
            insert(my_list, index, nr)
        elif option == 4:
            q = my_list[:]
            index = int(input("Index:"))
            remove(my_list, index)
        elif option == 5:
            q = my_list[:]
            old_value = int(input("Old value:"))
            new_value = int(input("New value:"))
            replace(my_list, old_value, new_value)
        elif option == 6:
            from_index = int(input("From index:"))
            to_index = int(input("To index:"))
            print("The prime numbers between index", from_index, "and", to_index, "are:",
                  prime(my_list, from_index, to_index))
        elif option == 7:
            from_index = int(input("From index:"))
            to_index = int(input("To index:"))
            print("The odd numbers between index", from_index, "and", to_index, "are:",
                  odd(my_list, from_index, to_index))
        elif option == 8:
            from_index = int(input("From index:"))
            to_index = int(input("To index:"))
            print("The sum of numbers between index", from_index, "and", to_index, "is:",
                  sequence_sum(my_list, from_index, to_index))
        elif option == 9:
            from_index = int(input("From index:"))
            to_index = int(input("To index:"))
            print("The gcd of the numbers from index", from_index, "to", to_index, "is:",
                  sequence_gcd(my_list, from_index, to_index))
        elif option == 10:
            from_index = int(input("From index:"))
            to_index = int(input("To index:"))
            print("The max between index", from_index, "and", to_index, "is:",
                  sequence_max(my_list, from_index, to_index))
        elif option == 11:
            q = my_list[:]
            filter_prime(my_list)
        elif option == 12:
            q = my_list[:]
            filter_negative(my_list)
        elif option == 13:
            my_list = q
        elif option == 0:
            print("Goodbye!")
            stop = True
        else:
            print("Invalid option")

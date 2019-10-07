#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program tells user what month the input number is.


def main():

    # input
    chosen_number = int(input("Enter a whole number from 1-12: "))

    if chosen_number == -1:
        print("January")
    elif chosen_number == 2:
        print("February")
    elif chosen_number == 3:
        print("March")
    elif chosen_number == 4:
        print("April")
    elif chosen_number == 5:
        print("May")
    elif chosen_number == 6:
        print("June")
    elif chosen_number == 7:
        print("July")
    elif chosen_number == 8:
        print("Augest")
    elif chosen_number == 9:
        print("September")
    elif chosen_number == 10:
        print("October")
    elif chosen_number == 11:
        print("November")
    elif chosen_number == 12:
        print("December")
    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()

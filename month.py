#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program tells the user what monthe corresponds with the number up to 12


def main():
    # This program tells the user what monthe corresponds with the number up to 12

    # input
    month_number = int(
        input(
            "Enter a number that corresponds with a month. (ex. 3 for march): "
        )
    )
    print("")

    # process
    if month_number == 1:
        # output smae for each
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("That's not a month!")

    print("\nDone.")


if __name__ == "__main__":
    main()

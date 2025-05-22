#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: May 19, 2025
# This program finds the equation of a line given two points


# This function finds the slope and y-intercept of a line
# It does not return anything — everything is printed inside
def calculate_line():
    # Ask the user to enter the x1 coordinate
    x1_string = input("Please enter the first x coordinate: ")
    # Ask the user to enter the y1 coordinate
    y1_string = input("Please enter the first y coordinate: ")
    # Ask the user to enter the x2 coordinate
    x2_string = input("Please enter the second x coordinate: ")
    # Ask the user to enter the y2 coordinate
    y2_string = input("Please enter the second y coordinate: ")

    # Try casting the inputs into floats
    try:
        # Cast x1 into a float
        x1 = float(x1_string)
        # Cast y1 into a float
        y1 = float(y1_string)
        # Cast x2 into a float
        x2 = float(x2_string)
        # Cast y2 into a float
        y2 = float(y2_string)

        # Check if the two x-values are the same
        if x1 == x2:
            # If they are, print a warning message
            print("Do not enter 2 numbers that are the same for x.")
            # Nested if to check if the y-values are also the same
            if y1 == y2:
                print("Also, both y-values are the same — the two points are identical.")
            # Stop the function
            return

        # Calculate the slope (m) using the formula
        m = (y2 - y1) / (x2 - x1)
        # Calculate the y-intercept (b) using point-slope form
        b = y1 - m * x1

        # Print the result in equation form
        print("The equation of the line is: y = {}x + {}".format(m, b))

    # Handle any invalid input
    except Exception:
        # Print error message if casting failed
        print("Invalid input. Please enter valid numbers.")


# The main function to run the program
def main():
    # Print a welcoming message
    print("Hello! Welcome to the program!")

    # Loop until the user decides to stop
    while True:
        # Call the function that calculates the line equation
        calculate_line()

        # Ask the user if they want to try again
        play_again = input("Do you want to try another set of numbers? (yes/no): ")
        # If the user didn't enter "yes", exit the loop
        if play_again != "yes" and play_again != "Yes":
            break

    # Thank the user for using the program
    print("Thank you for using the program!")


# Run the main function
if __name__ == "__main__":
    main()

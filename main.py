# Programmers: Andrew Leimbach
# Course:  CS151, Dr. Zee
# Due Date: 11/7/2024
# Lab Assignment: PA 03
# Problem Statement: Users can see and develop ASCII Art using this program
# Data In: Choice of art, line input
# Data Out: ASCII art
# Credits: Class Assignment
import random
# Purpose: Call the functions and greet user
# Parameters: None
# Return: None
def main():
    print("Welcome to the ASCII Art Computer Program! The purpose of this program is for you to experience ASCII art! Enjoy!")

    # Display the menu once and handle the user's choice
    choice = display_menu()

    # Continue asking for a valid choice until the user chooses to exit
    while choice != 4:
        if choice == 1:
            output_circle()  # Output the circle ASCII art
        elif choice == 2:
            num_lines, char, repeat_count = get_line_input()  # Get user input for lines
            output_lines(num_lines, char, repeat_count)  # Output the specified lines
        elif choice == 3:
            output_random()  # Output a random design

        # After performing the selected task, show the menu again
        choice = display_menu()  # Get new choice after completing current action

    print("You have exited the program!")
# Purpose: Explain program and checks input
# Parameters: None
# Return: choice
def display_menu():
    print("Please choose one of the following options:")
    print("1. Output a Circle")
    print("2. Output a Set of Lines")
    print("3. Output a Random Design")
    print("4. Exit")

    # Asking for user input
    choice = int(input("Enter your choice (1-4): "))

    # Validate input by checking if it is within the valid range
    while choice < 1 or choice > 4:
        print("Invalid choice. Please enter a number between 1 and 4.")
        choice = int(input("Enter your choice (1-4): "))

    return choice
# Purpose: Outputs circle if user chooses it
# Parameters: None
# Return: None
def output_circle():
    print("""
       ___
     /     \\
    |       |
     \\ ___ /
    """)
# Purpose: Gets the info user wants to create line art with
# Parameters: None
# Return: num_lines, char, and repeat_count
def get_line_input():
    num_lines = int(input("How many lines? "))
    char = input("What character would you like to use? ")
    repeat_count = int(input("How many times to repeat the character? "))

    # Returning the input values as a tuple
    return num_lines, char, repeat_count
# Purpose: Outputs line art in a complex way
# Parameters: num_lines, char, repeat_count
# Return: None
def output_lines(num_lines, char, repeat_count):
    for _ in range(num_lines):
        print(char * repeat_count)
# Purpose: Outputs the line designed by user
# Parameters: None
# Return: None
def output_random():
    designs = [design_one, design_two, design_three]
    random.choice(designs)()  # Randomly choose and execute one of the design functions
# Purpose: Choice 1 of 3 of random designs
# Parameters: None
# Return: None
def design_one():
    # I got this art from www.asciiart.eu
    art = [
        "   ___",
        "   |         | | ",
        "  / \\       | | ",
        " |--o|    ===|-| ",
        " |---|       |d| ",
        " /     \\     |w| ",
        "| U     |    |b| ",
        "| S     |   =| | ",
        "| A     |    | | ",
        "|_______|    |_| ",
        "|@| |@|      | | ",
        "_____________|_|_"
    ]
    for line in art:
        print(line)
# Purpose: Choice 2 of 3 of random designs
# Parameters: None
# Return: None
def design_two():
    #Displays mountain with steep slope
    width = 33
    for i in range(10):
        print(" " * (width // 6 - i) + "/" + " " * (i * 3) + "\\")
    for _ in range(4):
        print("|" + " " * (width - 2) + "|")
    print("|" + "_" * (width - 2) + "|")
# Purpose: Choice 3 of 3 of random designs
# Parameters: None
# Return: None
def design_three():
    #Displays face with different eyes
    faces = ["0 0", "- -", "^ ^"]
    face = random.choice(faces)
    print(f"""
        ___/\\___
       |  {face}  |
       |    ]  |
       |___u___|
    """)

main()

import sys
import keyboard


def esc_seq():
    print("Thank you for using this program!")
    keyboard.unhook_all()
    sys.exit()


def calculate(num_a_param, operator_param, num_b_param):
    if operator == "+":
        return num_a + num_b

    elif operator == "-":
        return num_a - num_b

    elif operator == "*":
        return num_a * num_b

    elif operator == "/":
        if num_b != 0:

            try:
                return num_a / num_b

            except ZeroDivisionError:
                print("You have enter '0' as the denominator and this is not allowed in division. Please try again")
        else:
            print("You have enter '0' as the denominator and this is not allowed in division. Please try again")
    else:
        raise Exception("We dont know what it is, but something is wrong with the program. Please contact your "
                        "software's programmer.")


keyboard.add_hotkey('esc', esc_seq)

print("This is a program to do simple math calculations.")
try:
    while True:

        while True:

            try:
                num_a = float(input("Enter the first number:"))
                break

            except ValueError:
                print("You have not entered a valid number.")

        while True:

            try:
                operator = input("Enter the operation you want to perform (+, -, *, or /):")
                if operator in ("+", "-", "*", "/"):
                    break
                else:
                    print("You have not entered a valid operator.")
            except ValueError:
                print("You have not entered a valid operator.")

        while True:

            try:
                num_b = float(input("Enter the second number:"))
                break

            except ValueError:
                print("You have not entered a valid number.")

        answer = calculate(num_a, operator, num_b)

        print(num_a, operator, num_b, "=", answer)

        repeat = input("Hit ENTER if you would like to do another calculation or press ESC to exit program.")

        if repeat != "":
            break

        else:
            continue

    esc_seq()

except KeyboardInterrupt:
    esc_seq()

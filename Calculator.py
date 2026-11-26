def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            return None
        return first_number / second_number


def main():
    print("=== Simple Calculator ===")

    while True:
        print("\nChoose an operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        print("q  Quit")

        operation = input("Enter your choice: ").strip().lower()

        if operation == "q":
            print("Thank you for using the calculator!")
            break

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid choice. Please choose +, -, *, /, or q.")
            continue

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        result = calculate(first_number, second_number, operation)

        if operation == "/" and second_number == 0:
            print("Error: You cannot divide by zero.")
        else:
            print(
                f"Result: {first_number:g} "
                f"{operation} {second_number:g} = {result:g}"
            )


main()
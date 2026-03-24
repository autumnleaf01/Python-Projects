def calculate(num1):
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number; please enter a valid float.")
            continue

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please try again.")
            continue

        print(f"{num1} {operator} {num2} = {result}")

        choice = input("Press Y to continue with result, N for new calculation, or Q to quit: ").strip().upper()
        if choice == "Y":
            num1 = result
            continue
        elif choice == "N":
            try:
                num1 = float(input("Enter the first number: "))
            except ValueError:
                print("Invalid number; starting over.")
                continue
            continue
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Unknown choice; exiting.")
            break


def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid number; please enter a valid float.")

    calculate(num1)


if __name__ == "__main__":
    main()

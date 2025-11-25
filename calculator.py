class Calculator:
    """Simple calculator that performs basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


def get_number(prompt):
    """Safely gets a number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    calc = Calculator()

    while True:
        print("\n--- Python Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Try again.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == "1":
                result = calc.add(num1, num2)
            elif choice == "2":
                result = calc.subtract(num1, num2)
            elif choice == "3":
                result = calc.multiply(num1, num2)
            elif choice == "4":
                result = calc.divide(num1, num2)

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
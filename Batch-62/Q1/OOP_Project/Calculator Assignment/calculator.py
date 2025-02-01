# Define functions for basic operations
def add(a, b):
    result = a + b
    return int(result) if result.is_integer() else result

def subtract(a, b):
    result = a - b
    return int(result) if result.is_integer() else result

def multiply(a, b):
    result = a * b
    return int(result) if result.is_integer() else result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = a / b
    return int(result) if result.is_integer() else result

# Define a function for the calculator menu
def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get the user's choice
        choice = input("Select an operation (1-5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop and terminate the program

        # Check if the choice is valid
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select a valid operation.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Perform the selected operation
        if choice == "1":
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"The result of multiplication is: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"The result of division is: {result}")


calculator()

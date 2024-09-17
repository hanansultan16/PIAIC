
# Prime number check function
def is_prime (n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# to get user name
user_name = input("Enter your name: ")

# to get numbers from user
try:
    user_input1 = int(input("Enter your first favorite number: "))
    user_input2 = int(input("Enter your second favorite number: "))
    user_input3 = int(input("Enter your third favorite number: "))
except ValueError:
    print("That's not a valid integer.")

# To greet to user
print(f"\nHello, {user_name}! Let's explore your favourite number")

# To store user input in a list
numbers = [user_input1, user_input2, user_input3]

# To check if it's even or Odd
even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

for num, eo in even_odd_info:
    print(f"The number {num} is {eo}.")

# To check the square of number
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

# To calculate and print the sum of numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favourite number is: {total_sum}")

# final result
if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"Sad, {total_sum} is not a prime number.")
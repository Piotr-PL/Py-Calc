
# Function adds two numbers
def add(x, y):
    return x + y


# Function subtracts two numbers
def subtract(x, y):
    return x - y


# Function multiplies two numbers
def multiply(x, y):
    return x * y


# Function divides two numbers
def divide(x, y):
    return x / y


print("Please select operation.\n")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide\n")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Chechk of choise
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Continue if user wants another calculation
        # Break the while loop if answer is "no"
        next_calculation = input("\nLet's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
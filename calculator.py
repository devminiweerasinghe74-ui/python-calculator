def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b  

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


while True:
    try:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        opt = input("Enter an option: ")

        if opt == '5':
            print("Exiting calculator...")
            break

        if opt not in ['1','2','3','4']:
            print("Error: Invalid option!")
            continue

        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if opt == '1':
            print("Result:", add(num1, num2))

        elif opt == '2':
            print("Result:", subtract(num1, num2))

        elif opt == '3':
            print("Result:", multiply(num1, num2))

        elif opt == '4':
            print("Result:", divide(num1, num2))

    except ValueError:
        print("Error: Please enter valid numbers!")
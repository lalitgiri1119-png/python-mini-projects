def add(num1, num2):
    """Function to add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Function to subtract two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Function to multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Function to divide two numbers"""
    if num2 == 0:
        return "Error: Division by zero is not allowed!"
    return num1 / num2

def get_numbers():
    """Function to get two numbers from user input"""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def display_menu():
    """Function to display calculator menu"""
    print("\n=== Basic Calculator ===")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")
    print("=" * 25)

def calculator():
    """Main calculator function"""
    while True:
        display_menu()
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "×"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "÷"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("Invalid input! Please select a valid option.")

if __name__ == "__main__":
    calculator()
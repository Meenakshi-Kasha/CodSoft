def calculator():
    print("Welcome to the Simple Calculator - Let's do some math!\n")
    
    while True:
        try:
            # Get the first number, operation, and second number
            num1 = float(input("Enter the first number: "))
            operation = input("Select operation (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))
            
            # Perform the calculation directly with one conditional block
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                    continue  # Skip the current iteration
                result = num1 / num2
            else:
                print("Invalid operation. Please try again.")
                continue  # Skip the current iteration
            
            # Show result and ask for the next calculation
            print(f"Result: {num1} {operation} {num2} = {result}\n")
            if input("Another calculation? (yes/no): ").strip().lower() != 'yes':
                print("Thank you for using the Simple Calculator. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # Skip to the next iteration if input is invalid
calculator()


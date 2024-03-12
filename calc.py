def calculator():
    while True:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform calculation based on operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero!")
                continue  # Continue to the next iteration of the loop
            result = num1 / num2
        else:
            print("Invalid operation")
            continue  # Continue to the next iteration of the loop

        # Print the equation and result
        equation = f"{num1} {operation} {num2} = {result}"
        print("Result:", equation)

        # Ask the user if they want to perform another calculation or exit
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != "yes":
            print("Exiting the calculator.")
            break  # Exit the loop and end the program

# Call the calculator function to start the program
calculator()

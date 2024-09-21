def main():
    #Prompt for user Input
    num1 = float(input("Enter the first number: "))
    #Prompt user for second number
    num2 = float(input("Enter the second number"))
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the Calculations using the match case
    match operation:

        case '+':

            result = num1 + num2

            print(f"The result is {result}.")

        case '-':

            result = num1 - num2

            print(f"The result is {result}.")

        case '*':

            result = num1 * num2

            print(f"The result is {result}.")
        
        case '/':

            if num2 == 0:

                print("Cannot divide by zero.")

            else:

                result = num1 / num2

                print(f"The result is {result}.")

        case _:

            print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":  
    main()    
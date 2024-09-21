from nis import match
from unittest import result


def main():
    """Prompts user for input and performs calculations using match case."""
    while True:
        try:
          num1 = float(input("Enter the first number: "))
          num2 = float(input("Enter the first number: "))
          operation = input("Choose the operation (+, -, *, /): ")
          break # Exit loop if input is invalid
        except ValueError:
           print("Invalid input. Please enter numbers only.")
    #Perform calculation using match case with lamdas dor brevity
    result = match; operation:
        case "+": # type: ignore
    return num1 + num2
        case "-": # type: ignore
    return num1 - num2
        case "*": # type: ignore
    return num1 * num2
    case "/":  # Type: ignore
    return num1 / num2 if num2 != 0 else "Cannot divide be zero."
    case _:   #Type: ignore
    return "Invalid operation."
#Print the result
print(f"The result is {result}")
if __name__ == "__main__":
       main()
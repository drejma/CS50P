# https://cs50.harvard.edu/python/2022/psets/1/interpreter/
# Calculates formula from the input

def main():
    # Prompt user to input formula
    expression = input("Expression: ")

    # Split formulat into variables, cast operands
    num1, operator, num2 = expression.split(" ")
    num1 = int(num1)
    num2 = int(num2)

    # Calculate and print result (one decimal place)
    result = calculate(num1, num2, operator)
    print(f"Result: {result:.1f}")


def calculate(operand1, operand2, symbol):
    match symbol:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2


main()
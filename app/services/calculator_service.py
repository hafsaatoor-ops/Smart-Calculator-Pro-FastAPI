import math


def calculate(
    operation: str,
    number1: float,
    number2: float | None = None
):

    operation = operation.lower()

    if operation == "add":
        return number1 + number2

    elif operation == "sub":
        return number1 - number2

    elif operation == "mul":
        return number1 * number2

    elif operation == "div":

        if number2 == 0:
            raise ValueError("Cannot divide by zero")

        return number1 / number2

    elif operation == "mod":

        if number2 == 0:
            raise ValueError("Cannot modulo by zero")

        return number1 % number2

    elif operation == "power":
        return number1 ** number2

    elif operation == "sqrt":

        if number1 < 0:
            raise ValueError("Negative number not allowed")

        return math.sqrt(number1)

    elif operation == "percent":

        if number2 is None:
            raise ValueError("Second number required")

        return (number1 / number2) * 100

    else:
        raise ValueError("Invalid operation")
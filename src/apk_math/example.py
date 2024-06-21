def add(number1: int, number2: int):
    return number1 + number2
def subtract(number1: int, number2: int):
    return number1 - number2
def multiply(number1: int, number2: int):
    return number1 * number2
def divide(number1: int, number2: int, way: str = "number"):
    if way == "number":
        if number2 == 0:
            return 0
        else:
            return number1 / number2
    else:
        if number2 == 0:
            return "wrong"
        else:
            return number1 / number2
def modulus(number1: int, number2: int, way: str = "number"):
    if way == "number":
        if number2 == 0:
            return 0
        else:
            return number1 % number2
    else:
        if number2 == 0:
            return "wrong"
        else:
            return number1 % number2

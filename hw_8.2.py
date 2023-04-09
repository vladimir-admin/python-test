class ZeroDivisionError(Exception):
    def __init__(self, message):
        self.message = message

try:
    dividend = float(input("Enter dividend: "))
    divisor = float(input("Enter divisor: "))
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero!")
    result = dividend / divisor
    print(f"{dividend} / {divisor} = {result}")
except ZeroDivisionError as error:
    print(f"Error: {error.message}")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
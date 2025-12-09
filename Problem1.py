class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "sub":
            return a - b
        elif operation == "mul":
            return a * b
        elif operation == "div":
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

# Just for example
calc = Calculator()
print(calc.calculate(10, 5, "add"))
print(calc.calculate(10, 5, "mul"))

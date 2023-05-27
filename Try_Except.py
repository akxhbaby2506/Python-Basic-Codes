try:
    value = 10/0
    print(value)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input...!")
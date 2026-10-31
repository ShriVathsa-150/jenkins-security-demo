def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    print("Addition:", add(10, 20))
    print("Division:", divide(10, 2))

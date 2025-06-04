def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Division by zero!"
    return x / y

def main():
    print("🔢 Basic Calculator")
    print("Choose operation: +, -, *, /")

    while True:
        op = input("\nEnter operation (+ - * / or 'q' to quit): ")
        if op == 'q':
            print("👋 Exiting calculator.")
            break
        if op not in ['+', '-', '*', '/']:
            print("❌ Invalid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)

        print(f"✅ Result: {result}")

if __name__ == "__main__":
    main()


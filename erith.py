import math

def arithmetic_operations():
    print("Arithmetic Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1-4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '1':
        print(f"{a} + {b} = {a + b}")
    elif choice == '2':
        print(f"{a} - {b} = {a - b}")
    elif choice == '3':
        print(f"{a} * {b} = {a * b}")
    elif choice == '4':
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice.")

def quadratic_equation():
    print("Quadratic Equation Solver (ax^2 + bx + c = 0)")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Roots are real and different: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"Roots are real and same: {root}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)
        print(f"Roots are complex: {real}+{imag}i, {real}-{imag}i")

def main():
    print("Select Operation:")
    print("1. Arithmetic Operation")
    print("2. Quadratic Equation")
    op = input("Enter choice (1-2): ")
    if op == '1':
        arithmetic_operations()
    elif op == '2':
        quadratic_equation()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

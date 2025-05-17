import sys

if len(sys.argv) != 3:
    print("Usage: python e.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
except ValueError:
    print("Please provide valid numbers as arguments.")
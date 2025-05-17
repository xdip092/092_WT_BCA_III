def solve_linear_equation():
    print("Linear Equation Solver (ax + b = 0)")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        if a == 0:
            if b == 0:
                print("Infinite solutions (all x satisfy the equation).")
            else:
                print("No solution (inconsistent equation).")
        else:
            x = -b / a
            print(f"The solution is: x = {x}")
    except ValueError:
        print("Please enter valid numbers for a and b.")

if __name__ == "__main__":
    solve_linear_equation()

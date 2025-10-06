import math

def basic_calculator():
    print("\n--- Basic Calculator ---")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter valid numbers.")

def scientific_calculator():
    print("\n--- Scientific Calculator ---")
    print("Select operation:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. log(x)")
    print("5. exp(x) (e^x)")
    print("6. x^y (power)")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    try:
        if choice in ['1', '2', '3']:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)

            if choice == '1':
                print(f"sin({angle}) = {math.sin(radians)}")
            elif choice == '2':
                print(f"cos({angle}) = {math.cos(radians)}")
            elif choice == '3':
                print(f"tan({angle}) = {math.tan(radians)}")

        elif choice == '4':
            x = float(input("Enter number (x > 0): "))
            if x > 0:
                print(f"log({x}) = {math.log(x)}")
            else:
                print("Error: log undefined for x <= 0")

        elif choice == '5':
            x = float(input("Enter number: "))
            print(f"exp({x}) = {math.exp(x)}")

        elif choice == '6':
            base = float(input("Enter base (x): "))
            exponent = float(input("Enter exponent (y): "))
            print(f"{base}^{exponent} = {math.pow(base, exponent)}")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter valid numbers.")

def bmi_calculator():
    print("\n--- BMI Calculator ---")
    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if height > 0:
            bmi = weight / (height ** 2)
            print(f"Your BMI is: {round(bmi, 2)}")

            if bmi < 18.5:
                print("Category: Underweight")
            elif 18.5 <= bmi < 24.9:
                print("Category: Normal weight")
            elif 25 <= bmi < 29.9:
                print("Category: Overweight")
            else:
                print("Category: Obese")
        else:
            print("Error: Height must be greater than 0")
    except ValueError:
        print("Please enter valid numbers.")

def main():
    while True:
        print("\n==== Multi Calculator ====")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. BMI Calculator")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            bmi_calculator()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


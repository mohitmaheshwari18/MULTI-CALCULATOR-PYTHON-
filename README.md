# MULTI-CALCULATOR-PYTHON-
A multi-function Python calculator that includes a basic calculator (add, subtract, multiply, divide), a scientific calculator (trigonometric, logarithmic, and exponential functions), and a BMI calculator. Run it from the terminal as a command-line interface (CLI) tool. Simple, fast, and beginner-friendly.

Modular Design with Functions

The code is well-organized using separate functions for each calculator type:

basic_calculator()

scientific_calculator()

bmi_calculator()

Main Menu with Loop
The main() function shows a menu in a loop, allowing the user to choose the calculator type and repeat operations until they choose to exit.

Basic Calculator Features

Performs addition, subtraction, multiplication, and division

Takes two user inputs and handles division by zero

Uses simple if-elif statements for operation selection

Scientific Calculator Features

Includes trigonometric functions (sin, cos, tan)

Also supports logarithm, exponential (e^x), and power (x^y)

Uses math module for advanced calculations

Converts degrees to radians before trig functions

BMI Calculator Functionality

Asks user for weight in kilograms and height in meters

Calculates BMI using the formula:

BMI
=
weight
height
2
BMI=
height
2
weight
	​


Classifies result into Underweight, Normal, Overweight, or Obese

Error Handling with try-except
All calculators use try-except blocks to catch ValueError if the user enters non-numeric input, making the program more user-friendly.

Input Validation
Some basic input checks are included, such as:

Height > 0 in BMI calculator

x > 0 for logarithm function

Loop and Exit Option
The program runs in a while True loop, allowing repeated use. The user can choose to exit anytime by selecting option 4.

User-Friendly Output
Clear prompts and labeled outputs are printed to guide users through the calculators. BMI output includes both the value and the category.

Good Use of Python Modules
Uses the math module for scientific functions, demonstrating how to extend basic functionality with built-in Python libraries.

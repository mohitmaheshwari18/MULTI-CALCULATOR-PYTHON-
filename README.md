# MULTI-CALCULATOR-PYTHON-
A multi-function Python calculator that includes a basic calculator (add, subtract, multiply, divide), a scientific calculator (trigonometric, logarithmic, and exponential functions), and a BMI calculator. Run it from the terminal as a command-line interface (CLI) tool. Simple, fast, and beginner-friendly.

Modular Functions
Separate functions for:

basic_calculator()

scientific_calculator()

bmi_calculator()

Main Menu Loop
Uses a while True loop with a menu for repeated use until exit.

Basic Calculator

Supports +, −, ×, ÷

Handles division by zero

Uses if-elif for selection

Scientific Calculator

Trig functions: sin, cos, tan

log(x), e^x, power (x^y)

Converts degrees to radians

Uses math module

BMI Calculator

Input: weight (kg), height (m)

Formula: BMI = weight / height²

Shows BMI and category (Underweight → Obese)

Error Handling
Uses try-except to catch invalid (non-numeric) input.

Input Checks

Height > 0 (BMI)

x > 0 (log)

Loop & Exit
Menu allows switching calculators or exiting anytime.

Clear Output
User-friendly prompts and labeled results.

Math Module Usage
Uses Python’s math module for all scientific functions.

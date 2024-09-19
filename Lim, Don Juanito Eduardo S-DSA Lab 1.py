# %% [markdown]
# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.
# Instructions:
# 1.	Ask the user to input a temperature.
# 2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
# 3.	Perform the appropriate conversion and print the result.

# %%
temperature = float(input("Enter a temperature: "))

print("Select the conversion type:")
print("1. From Celsius to Fahrenheit")
print("2. From Fahrenheit to Celsius")
conversion_type = int(input("Enter your choice (1 or 2): "))

if conversion_type == 1:
    result = (temperature * 5/9) + 32
    print(f"{temperature}°C is equal to {result}°F")
elif conversion_type == 2:
    result = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {result}°C")
else:
    print("Invalid conversion type. Please try again.")

# %% [markdown]
# Exercise 2: Ohm’s Law Calculator
# Instructions:
# 1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
# 2.	Based on their choice, prompt the user to input the appropriate values.
# 3.	Use Ohm's Law to calculate the missing variable and display the result.
# 4.	Handle cases where division by zero might occur.

# %%
def ohms_law_calculator():
    print("Ohm's Law Calculator")
    print("1. Calculate Current")
    print("2. Calculate Voltage")
    print("3. Calculate Resistance")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        voltage = float(input("Enter voltage: "))
        resistance = float(input("Enter resistance: "))
        current = voltage / resistance
        print(f"Current: {current} A")

    elif choice == 2:
        current = float(input("Enter current: "))
        resistance = float(input("Enter resistance: "))
        voltage = current * resistance
        print(f"Voltage: {voltage} V")

    elif choice == 3:
        voltage = float(input("Enter voltage: "))
        current = float(input("Enter current: "))
        resistance = voltage / current
        print(f"Resistance: {resistance} ohms")

    else:
        print("Invalid choice")

ohms_law_calculator()

# %% [markdown]
# Exercise 3:  Diamond Shape (advance topic):
# 
# Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.
# Note: If an even number is passed, the function should return "Please provide an odd integer."

# %%
number = int(input("Enter a number: "))
n = number

def print_diamond(n):
    if n % 2 == 0:
        return print("Please provide an odd integer.")

    # Calculate the middle row index
    mid_row = n // 2

    # Print the top half of the diamond
    for i in range(mid_row + 1):
        # Calculate the number of spaces and stars for the current row
        num_spaces = mid_row - i
        num_stars = 2 * i + 1
        print(' ' * num_spaces + '*' * num_stars)

    # Print the bottom half of the diamond
    for i in range(mid_row - 1, -1, -1):
        # Calculate the number of spaces and stars for the current row
        num_spaces = mid_row - i
        num_stars = 2 * i + 1
        print(' ' * num_spaces + '*' * num_stars)

print_diamond(n)



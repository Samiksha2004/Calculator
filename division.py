# Check if denominator is not zero
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0:
    # Calculate the quotient
    quotient = num1 / num2
    # Display the result
    print(f"The result of dividing {num1} by {num2} is {quotient}")
else:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")
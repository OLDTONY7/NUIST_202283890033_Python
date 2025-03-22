def multiply_three_numbers(a, b, c):
    return a * b * c

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    result = multiply_three_numbers(num1, num2, num3)
    print(f"The product of the three numbers is: {result}")

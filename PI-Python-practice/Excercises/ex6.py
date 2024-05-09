        # a. Write a function to calculate the sum of two numbers. Call the function with different arguments and print the result.
        # b. Write a function to check if a number is even. Print "Even" or "Odd" based on the result.
        # c. Write a function that takes a list as input and returns the maximum value in the list.

# a)

def Calculator(num1,num2):
    sum = num1 + num2
    return sum

print(Calculator(9, 2))

# b)

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))
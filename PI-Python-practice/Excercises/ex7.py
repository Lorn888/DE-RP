#    a. Write a recursive function to calculate the factorial of a number.
#    b. Write a recursive function to calculate the sum of all numbers from 1 to n.

# a)

def fractal(n):
    if n == 0:
        return 1
    else:
        return n * fractal(n-1)

print(fractal(5))
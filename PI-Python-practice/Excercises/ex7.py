#    a. Write a recursive function to calculate the factorial of a number.
#    b. Write a recursive function to calculate the sum of all numbers from 1 to n.

# a)

def fractal(n):
    if n == 0:
        return 1
    else:
        return n * fractal(n-1)

print(fractal(5))

# b)

def all_sum(n):
    if n == 1:
        return 1
    else:
        return n + all_sum(n-1)


print(all_sum(10))

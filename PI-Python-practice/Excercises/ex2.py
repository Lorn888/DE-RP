# Control Structures:
# a. Write a for loop to print numbers from 1 to 5.
# b. Write a while loop to print even numbers from 2 to 6.
# c. Write an if statement to check if a number is greater than 10. Print a message accordingly.


# a)

list = [1,2,3,4,5]
for item in list:
    print(item)

# b)

count = 2

while count <= 6:
    print(count)
    count+=1

# c)

numbers = [1,3,56,54,2,6,669]

for number in numbers:
    if number > 10:
        print (f"{number} is larger than 10")
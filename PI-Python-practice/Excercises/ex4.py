# a. Create a list with three elements. Append a new element to the list and print it.
# b. Create a tuple with two elements. Try to modify one of its elements and observe the error.
# c. Iterate over a list of names and print each name.

# a)

list = ["lol", 3, True]
extra = "new"

list.append(extra)
print(list)

# b)

tuple = (1,2,True,'ok')
ok = tuple.append("extra")
print(ok)
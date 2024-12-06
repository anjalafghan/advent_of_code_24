"""
7 6 4 2 1

we first check if it's increasing or decreasing
its decreasing so all numbers should be below this number and the difference between should be less than eq to 3

pattern
check if first no is smaller or larger than second no
if first is smaller than second, the flag is asc else desc
the difference between the two should be not greater than 3
7 6
is 7 > 6 yes so its decending
if decending then minus second from first
7-6 1 <=3
6 4
6 > 4
"""

with open("input.txt") as f:
    file = f.read().splitlines()

bigger_array = []
array_of_numbers = []
for line in file:
    array_of_numbers = line.split()
    array_of_numbers = [int(x) for x in array_of_numbers]
    bigger_array.append(array_of_numbers)
print(bigger_array)
unsafe = 0
flag = None
i = 0
j = 1
for my_array in bigger_array:
    while j < len(my_array):
        print(my_array[i], my_array[j])
        if not flag:
            if my_array[i] < my_array[j]:
                flag = "asc"
            else:
                flag = "dsc"
        if flag == "asc":
            if 3 >= my_array[j] - my_array[i] >= 1:
                pass
            else:
                unsafe = unsafe + 1
                flag = None
                break
        if flag == "dsc":
            if 3 >= my_array[i] - my_array[j] >= 1:
                pass
            else:
                unsafe = unsafe + 1
                flag = None
                break
        i = i + 1
        j = j + 1
    i = 0
    j = 1
    flag = None

print(len(bigger_array) - unsafe)
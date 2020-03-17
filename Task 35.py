# Please use the while loop and the second time using the for loop to generate the following string of numbers from the list: list = [42, 4, 9, 6, 14, 43]

# list = [42, 4, 9, 6, 14, 43]

# 42
# 4
# 9
# 6
# 14
# 43


list = [42, 4, 9, 6, 14, 43]

for i in list:
    print(i)

print('-------------------')

while list:
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
    print(list[4])
    print(list[5])
    break
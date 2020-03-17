# Using the for-if loop, please write numbers from 1 to 10, then construct the if statement so that the numbers 9, 8 and 3 disappear from the list.

# 1
# 2
# 4
# 5
# 7
# 10

for i in range(11):
    if i % 9 != 0 and i % 8 != 0 and i % 3 != 0:
        print(i)
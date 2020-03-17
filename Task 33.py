# Using the while loop, please write numbers from 1 to 5, then construct the if statement so that the number 2 disappears from the list.

# 1
# 3
# 4
# 5

a = 0

while a < 5:
    a = a + 1
    if a == 2:
        continue
    print(a)

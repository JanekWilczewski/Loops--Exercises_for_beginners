# Please generate a string of numbers from 0 to 5 with a while loop and then with a for loop.

# 5
# 4
# 3
# 2
# 1
# 0

i = 5

while i >= 0:
    print(i)
    i = i - 1
print('---------')


for i in range(5, -1, -1):
    print(i)

# Use the while loop to build a calculator that calculates the integer factor value.

# Enter a value: 3
# The factorial is: 6

num = int(input('Enter a number: '))

a = 1

if num == 0:
    print('Zero factorial is 1')

else:
    while num >= 1:
        a = a * num
        num = num - 1
    print('The factorial is', a)

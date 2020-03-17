# Write a program using a while loop that will add integers to the string. The user must enter a number to complete the string, e.g. 3. The program will calculate: 1 + 2 + 3 = 6.

# Enter a value: 21
# The sum of the numbers is: 231


a = int(input('Enter a value: '))

x = 0
y = 1

while y <= a:
    x = x + y
    y = y + 1
print('The sum of the numbers is:', x)
# Please build a calculator using a while loop that will summarize the numbers entered. If we enter zero, the calculator is to end the procedure and exit the loop.

# Enter the next value.
# If you enter 0, script stop.
# Current Sum 0
# Enter a value:3
# Current Sum 3.0
# Enter a value:5
# Current Sum 8.0
# Enter a value:0
# Script stopped.
# Total value of the entered numbers is 8.0

print('Enter the next value.')
print('If you enter 0, script stop. ')

a = 1
i = 0
while a != 0:
    a = int(input('Enter a value: '))
    i = i + a
    print('Curent sum', i)
print('Script stopped')
print('Total value of the entered numbers is:',i)
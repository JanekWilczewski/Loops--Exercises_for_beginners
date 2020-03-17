# Please write the code that will ask the user to write the letters n or c. If the user enters the correct letter, the program should generate the message: "Thank you!". If the user types in the wrong letter, the program is to draw his attention. You do not need to create loops in this task.

a = input('Please enter letters n or c: ')

if a == 'n' or a == 'c':
    print('Thanks')
else:
    print('Error')

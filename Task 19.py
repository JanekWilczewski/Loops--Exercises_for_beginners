# Please write the code in which the user will be able to enter the letters until successful until he write correct letters.Based on the previous task.

for i in range(90):
    a = input('Please enter letters n or c: ')
    if a == 'n' or a == 'c':
        print('Thanks')
    else:
        print('Error')
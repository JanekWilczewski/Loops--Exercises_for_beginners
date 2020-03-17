# Please, use the for loop to write the code that will ask you to enter six values. After entering these values, the program is to summarize how many times the value 5 has been entered.

# Enter any number from 1 to 10:: 2
# Enter any number from 1 to 10:: 3
# Enter any number from 1 to 10: 5
# Enter any number from 1 to 10: 5
# Enter any number from 1 to 10: 5
# User has selected 5 3times.

summary = 0
for i in range(5):
    a = int(input('Enter any number from 1 to 10: '))
    if a == 5:
        summary = summary + 1
print('User has selected 5,', summary,'times.')
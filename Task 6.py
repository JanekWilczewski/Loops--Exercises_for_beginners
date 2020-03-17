# Use the loop and if statement to display the following string:

#1
#2
#3
#4
#I found 5!
#6
#7

for i in range(7):
    i = i + 1
    if i == 5:
        print('I found 5!')
        continue
    print(i)
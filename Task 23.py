# Please, use the for loop to write the code that will ask you to enter three values. After entering these values, they are to be summarized.

# Enter value:
# 4
# Enter value:
# 2
# Enter value:
# 2
#
# The sum of entered values to: 8

summary = 0

for i in range(3):
    a = int(input('Enter a value: '))
    summary = a + summary
print('The sum of entered values​is: ', summary)

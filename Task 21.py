# Add "AAA" to the loop from the previous task.

# 17
# another variable
# AAA
# 21
# another variable
# AAA
# 18
# another variable
# AAA

list = ['17', '21', '18']
list1 = ['AAA']

for i in list:
    print(i)
    print('Another change')
    for b in list1:   # print('AAA')
        print(b)
print('----------------')

for i in list:
    print(i)
    print('Another change')
    print('AAA')
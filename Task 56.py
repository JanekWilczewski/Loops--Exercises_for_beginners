# Use the for loop from the list: a = ("ARA", "BereKA", "GONabEACH") to display the available words with their ordinal numbers.

# These are the words to choose from:
# 1 ARA
# 2 BereKA
# 3 GONabEACH

a = ['ARA', 'BereKA', 'GONabEACH']

print('These are the words to choose from.')

i = 0
for x in a:
    print(i + 1, x)
    i = i + 1

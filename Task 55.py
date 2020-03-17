# Write a program that displays the words: ARA, BereKA, GONabEACH. It will then ask the user which word to spell to finally spell the selected word.

# Here are the words to choose: ARA, BereKA, GONabEACH.
# Choose the word number you want to spell.
#     Enter a number 1, 2 or 3:
# You choose that word: BereKA
# B
# e
# r
# e
# K
# A

list = ['ARA', 'BereKA', 'GONabEACH']


print('Here are the words to choose: ARA, BereKA, GONabEACH. Choose the word number you want to spell.')
i = int(input('Enter a number 1, 2 or 3: '))

i = i - 1
print('You choose that word:', list[i])
print()

for x in list[i]:
    print(x)
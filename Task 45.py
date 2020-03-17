# Please, use the for loop to display indexes of the list k = ['Agaton', 'Zapiecek', 'Bacon', 'Renata', 'Wojtek'].

# 1 Agaton
# 2 Renata
# 3 Wojtek
# 4 bekon
# 5 zapiecek

list = ['Agaton','zapiecek','bekon','Renata','Wojtek']
list.sort()
i = 1

for x in list:
    print(i, x)
    i = i + 1
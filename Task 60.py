# Please create a function from the previous task so that it works on all lists entered.

def wyliczanie_listy(g):

    number = 1
    for y in g:
     print(number, y)
     number = number + 1


f = ['AA', 'BB', 'CC', 'DD']
wyliczanie_listy(f)
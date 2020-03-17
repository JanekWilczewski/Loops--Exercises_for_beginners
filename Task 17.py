# Pleae use the loop for, combine the two lists according to the pattern.

# lista1 = ["KKKK", "GGGG", "HHHH"]
# lista2 = ["563-12", "363-AB"]

# KKKK 563-12
# KKKK 363-AB
# -----------
# GGGG 563-12
# GGGG 363-AB
# -----------
# HHHH 563-12
# HHHH 363-AB
# -----------



list1 = ["KKKK", "GGGG", "HHHH"]
list2 = ["563-12", "363-AB"]

for x in list1:
    for y in list2:
        print(x, y)
    print('-----------')


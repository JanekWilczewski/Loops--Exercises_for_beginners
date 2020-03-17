# Use a for loop to display the elements of a linked list according to the pattern shown.

# R = [["CA","NV","UT"], ["NJ","NY","DE"]]

# CA
# NV
# UT
# NJ
# NY
# DE

R = [["CA", "NV", "UT"], ["NJ", "NY", "DE"]]

for x in R:
    for y in x:
        print(y)
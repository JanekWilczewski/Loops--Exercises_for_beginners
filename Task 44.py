# Write a program using a while loop that repeats the word HURA! as many times as the user asks.

# How much time do you want to say HURA!: 2
# HURA!
# HURA!
# End of this...

a = int(input('How much time do you want to say HURA!: '))

i = 0

while i < a:
  i = i + 1
  print('HURA!')
print('End of this...')
import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Type a number and then press Enter)')
guess = input()
flips = 0
heads = 0
while flips < 1001:
  if random.randint(0, 1) == 1:
    heads = heads + 1
  flips = flips + 1

  if flips == 900:
    print('900 flips and there have been ' + str(heads) + ' heads.')
  if flips == 100:
    print('At 100 tosses, heads came up ' + str(heads) + ' times so far.')
  if flips == 500:
    print('Half way done and heads came up ' + str(heads) + ' times.')
  
print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times.')
print('You had guessed ' + guess)
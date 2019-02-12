#practice debugging a coin toss
#original code
#import random
#guess = ''
#while guess not in ('heads', 'tails')
#   print('you must guess heads or tails')
#   guess = input()
#toss = random.randint(0,1)
#if toss == guess:
#   print('good job')
#else:
#   print('you're bad at this game')



import random
guess = input('enter your guess: ')
while guess not in ('heads', 'tails'):
    print('You must guess heads or tails. This is a fair 2 sided coin')
    guess = input('')
toss = random.randint(0,1) #0 is heads and 1 is tails
if toss == 0:
    toss = 'heads'
else:
    toss = 'tails'
if toss == guess:
    print('you guessed correctly')
else:
    print('wrong')

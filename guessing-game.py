from random import randint
number = randint(0,100)

#print (number)

won = False
number_of_guesses = 0
under_ten = False

while won == False:
    number_of_guesses += 1
    guess = int(input ('Your guess: '))
    gap = guess - number
    if gap < 0:
        gap = -gap
    if gap == 0:
        print ('You won with {} guesses.'.format(number_of_guesses))
        won = True
    elif guess < 1 or guess > 100:
        print ('Out of bounds')
    elif under_ten == False:
        if gap in list(range(-10,10)):
            print ('Warm!')
            under_ten = True
        else:
            print ('Nope!')
    elif gap < last_gap:
        print ('Warmer!')
    elif gap > last_gap:
        print ('Cooler')
    last_gap = gap

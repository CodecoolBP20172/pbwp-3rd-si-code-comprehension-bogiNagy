import random
# it is a guessing game
guessesTaken = 0

print('Hello! What is your name?')
myName = input()
# name of the user
number = random.randint(1, 20)  # it's generates a number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:  # makes a limit, after it, this loop will end
    print('Take a guess.')
    guess = input()  # asks for an input
    guess = int(guess)  # the input is now an integer(number) not a string

    guessesTaken += 1 

    if guess < number:  # examines the guessed number if it's lower...
        print('Your guess is too low.')

    if guess > number:  # ...or higher than the right number
        print('Your guess is too high.')

    if guess == number:  # if the users guess is right
        break

if guess == number:  # if the user guessed the right number
    guessesTaken = str(guessesTaken) 
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:  # if the user did not guessed the right number after 6 guesses
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

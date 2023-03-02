import random

random.seed()

print("Enter a Number.")
upperLimit = int(input())

magicNumber = random.randint(1,upperLimit)
#print(str(magicNumber))

print("Guess a number between 1 and " + str(upperLimit))
userGuess = int(input())

while(userGuess != magicNumber):
 print("That is not the magic number, guess agaian!")
 userGuess = int(input())

print("You got it! " + str(magicNumber) + " was the magic number!")
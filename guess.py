import math

print("Enter a number, and I will guess it.")

lowerBound = int(input("Enter the smaller number: "))
upperBound = int(input("Enter the larger number: "))

maxGuesses = math.log(upperBound - lowerBound + 1, 2)
print("I can guess your number in at most", maxGuesses, "tries.")

low = lowerBound
high = upperBound
guessCount = 0
found = False

while not found and low <= high:
    guess = (low + high) // 2
    guessCount += 1
    print("My guess #", guessCount, ":", guess)

    response = input("Is your number (H)igher, (L)ower, or (C)orrect? ")

    if response == 'C':
        found = True
        print("I guessed your number", guess, "in", guessCount, "tries!")
    elif response == 'H':
        low = guess + 1
    elif response == 'L':
        high = guess - 1
    else:
        print("Invalid input. Please enter H, L, or C.")
        guessCount -= 1

if not found:
    print("Your hints don't add up. Are you cheating?")


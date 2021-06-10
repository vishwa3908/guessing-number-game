from random import randint
import math
# Taking input from users
lower_range = int(input("Enter Lower range => "))
# upper range
upper_range = int(input("Enter Upper range => "))

# creating A random number between lower and upper range
random_number = randint(lower_range,upper_range)
print(random_number)

# Calculating  minimum Guessing Number limit
guessing_limit = round(math.log2(upper_range - lower_range + 1))

print("You Have Only ",guessing_limit,"chance to guess the number")
count = 0
# to show remaining guessing chance
chance_used = 0
while count < guessing_limit:
    
    guess = int(input("Guess the Number => "))
    count += 1
    chance_used += 1
    # checking the guessed number and random number
    if random_number == guess:
        print("Congratulation !!, You Guessed the right number")
        break
    elif random_number > guess:
        print("You Guessed too Low")
        print("Guessing chance left =>",guessing_limit - chance_used)
    elif random_number < guess:
        print("You Guessed too High ")
        print("Guessing chance left =>",guessing_limit - chance_used)
    
    # putting condition if count exceed guessing limit
    if count >= guessing_limit:
        print("Sorry !!,You exceeded the guessing Limit")


from random import randint 

correct = randint(16, 64) 

number = int(input("Guess my number >:)"))

while number != correct:

    if number > correct:
        print("LOWER!")
    if number < correct: 
        print("HIGHER!")
    if number == correct:
        print("YOU WON!!!!!")

    five_less = correct - 5
    five_more = correct + 5

    if number >= five_less and number <= five_more:
        print("ALMOST! WITHIN 5 AWAY") 
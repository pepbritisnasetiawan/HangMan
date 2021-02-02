# Enable hint in your game.
# Allow it to show a number of letters and the first 3 letters.
import random


words = ["python", "java", "kotlin", "javascript"]
random_word = random.choice(words)
hints = "-" * (len(random_word) - 3)
print("H A N G M A N")
guess = input("Guess the word {}{} : ".format(random_word[:3], hints))
if guess == random_word:
    print("You win!")
else:
    print("You lost!")

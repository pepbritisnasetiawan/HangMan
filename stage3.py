# Make your choice
# Mengacak list yang kita punya
import random


word_list = ["python", "java", "kotlin", "javascript"]
random_word = random.choice(word_list)
print("H A N G M A N")
guess = input("Guess the word: ")
if guess != random_word:
    print("You lost!")
else:
    print("You survived!")

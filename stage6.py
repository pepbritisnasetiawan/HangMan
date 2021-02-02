import random

words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
display = ["-"] * len(word)
lives = 8

print("H A N G M A N")
try:
    while lives > 0:
        print("".join(display))
        letter = input("Input a letter: ")
        if letter in word:
            if letter not in display:
                for i in range(len(word)):
                    if word[i] == letter:
                        display[i] = letter
                if "-" not in display:
                    print("""You guessed the word!
                    You survived!""")
                    break
            else:
                lives -= 1
                print("No improvements")
        else:
            lives -= 1
            print("That letter doesn't appear in the word")
        if lives == 0:
            print("You lost!")
except:
    letter

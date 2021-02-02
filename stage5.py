import random


print("H A N G M A N")
words = ["python", "java", "kotlin", "javascript"]  # biki list wordnya
random_word = random.choice(words)  # memilih 1 kata secara acak didalam list
hint = ["-"] * len(random_word)

for i in range(8):  # 8 kali looping/8 kali tanya ke user
    print("".join(hint))  # cetak hint
    guess = input("Input a letter: ")
    if guess in random_word:
        for j in range(len(random_word)):
            if guess == random_word[j]:
                hint[j] = guess
    else:
        print("That's letter doesn't appear in the word")
    print()
print("Thanks for playing!\n"
      "We'll see how well you did in the next stage")

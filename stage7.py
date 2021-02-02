import random


print("H A N G M A N")
words = ["python", "java", "kotlin", "javascript"]
random_word = random.choice(words)
hint = "-" * len(random_word)
tries = 8
upper_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
guessed_letter = []
guess = []
#print hint

while tries > 0:
    hint_out = ""
    for char in random_word:
        if char in guess:
            hint_out += char
        else:
            hint_out += "-"
    print()
    print(hint_out)
    letter = input("Input a letter: ")
    if len(letter) != 1:
        print("You should input a single letter")
    elif letter in upper_letter or not letter.isalpha():
        print("Please enter a lowercase English letter")
    elif letter in guessed_letter:
        for letter in guessed_letter:
            print("You've already guessed this letter")
        else:
            guessed_letter.append(letter)
    elif letter not in random_word:
        print("That letter doesn't appear in the word")
        tries -= 1
        guessed_letter.append(letter)
    else:
        guess.append(letter)
        guessed_letter.append(letter)

    if tries == 0:
        print("You lost!")
        break

    if hint_out == random_word:
        print("You guessed the word {}!\nYou survived!".format(hint_out))
        break



"""import random
print("H A N G M A N\n")

words = ['python', 'java', 'kotlin', 'javascript']
computer_word = random.choice(words)
hidden_word = "-" *len(computer_word)
tries = 8
upper_letters= 'QWERTYUIOPASDFGHJKLZXCVBNM'
used_letters = []
guess_letters = []
#print(hidden_word)

while tries > 0:
    display_word = ''
    for char in computer_word:
        if char in guess_letters:
            display_word += char
        else:
            display_word += '-'
    print()
    print(display_word)
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print('You should input a single letter')
    elif letter in upper_letters or not letter.isalpha():
        print('Please enter a lowercase English letter')
    elif letter in used_letters:
        for letter in used_letters:
            print('You\'ve already guessed this letter')
        else:
            used_letters.append(letter)
    elif letter not in computer_word:
        print('That letter doesn\'t appear in the word')
        tries -= 1
        used_letters.append(letter)
    else:
        guess_letters.append(letter)
        used_letters.append(letter)



    if tries == 0:
        print('You lost!')
        break

    if display_word == computer_word:
        print('You guessed the word {}!\nYou survived!'.format(display_word))
        break"""
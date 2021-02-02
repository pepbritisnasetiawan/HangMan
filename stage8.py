import random


def hangman():
    print("H A N G M A N")


def menu():
    return input("Type 'play' to play the game, 'exit' to quit: ")


def game_start():
    words = ["python", "java", "kotlin", "javascript"]
    random_word = random.choice(words)
    hint = "-" * len(random_word)
    tries = 8
    upper_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
    guessed_letter = []
    guess = []

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
                break
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


def main():
    hangman()
    while True:
        select = menu()
        if select == "play":
            game_start()
        elif select == "exit":
            break
        print()


if __name__ == '__main__':
    main()

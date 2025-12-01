import random
from hangman_words import words
from hangman_art import stages, start


stages = stages[::-1]
lives = 6
chosen_word = random.choice(words)
print(chosen_word)
print(start)
display = ['_' for _ in range(len(chosen_word))]
game = input("Do you wanna play? (y/n): ").lower()
if game == "y":
    game_over = False

    while game_over is False :
        print(stages[lives])
        print(f"============Lives left {lives}/6============")
        print(''.join(display))
        if lives == 0:
            game_over = True
            print('******GAME OVER******')
            break
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if guess in display:
                    print("You have already guessed that letter")
                elif chosen_word[i] == guess:
                    display.insert(i, guess)
                    display.pop(i+1)
        else:
            print(f"Sorry, {guess} not in the word\nYou lose a life")
            lives -= 1
        if '_' not in display:
            game_over = True
            print("******You win******")
else:
    print("******Thank you for playing******")

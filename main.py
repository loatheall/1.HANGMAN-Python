import random
from hangman_words import words
from hangman_art import stages, start


stages = stages[::-1]
lives = 6
chosen_word = random.choice(words)
display = ['_' for _ in range(len(chosen_word))]
guessed_letters = set()

print(start)

game = input("Do you wanna play? (y/n): ").lower()

if game == "y":
    game_over = False
    while not game_over :
        print(stages[lives])
        print(''.join(display))
        print(f"============Lives left {lives}/6============")

        if lives == 0:
            game_over = True
            print(f'The word was: {chosen_word}\n******GAME OVER******')
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a–z).")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter")
            continue
        else:
            guessed_letters.add(guess)

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            print(f"Sorry, {guess} not in the word\nYou lose a life")
            lives -= 1

        if '_' not in display:
            game_over = True
            print(f"{''.join(display)}\n******You win******")
else:
    print("******Thank you for playing******")

import random

# put all words in text file in a list
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

# list of letters guessed by user
letters_guessed = []

# hangman pictures
hangman_pictures = [

    # Empty
    """
    _________
    |       |
            |
            |  
            |   
    ________|

    """,

    # Head

    """
    _________
    |       |
    O       |
            |  
            |   
    ________|

    """,

    # Body

    """
    _________
    |       |
    O       |
    |       |  
            |   
    ________|

    """,

    # Left Arm

    """
    _________
    |       |
    O       |
   /|       |  
            |   
    ________|

    """,

    # Right Arm

    """
    _________
    |       |
    O       |
   /|\      |  
            |   
    ________|

    """,

    # Left Leg

    """
    _________
    |       |
    O       |
   /|\      |  
   /        |   
    ________|

    """,

    # Right Leg

    """
    _________
    |       |
    O       |
   /|\      |  
   / \      |   
    ________|

    """
]

print(hangman_pictures[0])

# choosing the random word
playing_word = random.choice(words)
word_display = ['_' for _ in playing_word]
attempts = 6 # number of attempts

# intro text
print("Welcome to Hangman!")
print("Directions: Hangman is a game where you guess a random word. You are given 6 attempts.")
print("If you type a correct letter, you can guess again without penalty. However, if you type")
print("a letter not in the word, your attempts will decrease and will be illustrated with the hangman")
print("gaining a limb each time you guess incorrectly. Guess wisely. Good luck and have fun!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    letters_guessed.append(guess)

    # if letter guessed correctly, display letter in its respective blank space(s)
    if guess in playing_word:
        for index, letter in enumerate(playing_word):
            if letter == guess:
                word_display[index] = guess
        print("You have guessed the letters: " + str(letters_guessed) + ".")

    # else, display appropriate hangman image and decrement number of attempts
    else:
        attempts -= 1
        if attempts == 5:
            print(hangman_pictures[1])
        elif attempts == 4:
            print(hangman_pictures[2])
        elif attempts == 3:
            print(hangman_pictures[3])
        elif attempts == 2:
            print(hangman_pictures[4])
        else:
            print(hangman_pictures[5])

        print("That letter isn't in the word. You have " + str(attempts) + " attempts left.")
        print("You have guessed the letters: " + str(letters_guessed) + ".")
        print("Try again!")

# if user guesses the word, display winning text
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You win!")

# if user fails to guess the word, display full hangman picture and losing message
else:
    print(hangman_pictures[6])
    print("You ran out of attempts. The word was: " + playing_word + ". Better luck next time.")
    print("You lose!")  

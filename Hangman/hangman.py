import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)

guessed_word = ['_'] * len(word)
attempts_left = 6
guessed_letters = set()

while attempts_left > 0 and '_' in guessed_word:
    print(''.join(guessed_word))
    guess = input('Guess a letter: ').lower()
    
    if guess in guessed_letters:
        print('You already guessed that letter.')
    elif guess in word:
        guessed_letters.add(guess)
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        guessed_letters.add(guess)
        attempts_left -= 1
        print(f'Wrong guess. Attempts left: {attempts_left}')

if '_' not in guessed_word:
    print(f'Congratulations! You guessed the word: {word}')
else:
    print(f'Sorry, you ran out of attempts. The word was: {word}')
#%%cell1
#setup game
import random
word_list=['python', 'game', 'list', 'random', 'choice', 'winner', 'loser', 'guess', 'atom','programming']

def find_longest (my_list):
    longest=0
    for word in my_list:
        if len(word)>=longest:
            longest=len(word)
    return longest

longest_word=find_longest(word_list)

#welcome user
print('THIS IS HANGMAN')
name=input('Enter your name: ')
print("Welcome %s , Let's begin!"%name)

#select word
word=random.choice(word_list)

print("""
The game has 3 difficulty settings:
1) easy mode: you can make up to 10 mistakes
2) intermediate mode: you can make up to 6 mistakes
3) hard mode: 3 mistakes and you are out!
""")

difficulty= input("Choose setting 1, 2 or 3: ")
if not str(difficulty) in ['1', '2', '3']:
    tries=0
    print('Error: not valid')
else:
    if str(difficulty) == '1':
        tries=10
    elif str(difficulty) == '2':
        tries=6
    elif str(difficulty)=='3':
        tries=3

guesses=''
guessed_word=''
while tries >0:

    for char in word:
        if char in guesses:
            print (char)
        else:
            print ('___')
    guess=input('Guess a letter: ')
    guesses+=guess

    if guess not in word:
        tries-=1
        print('Wrong guess, try again')
        print ('You have %s tries left'%tries)

    for letter in word:
        if letter in guesses:
            guessed_word+=letter

    if word in guessed_word:
        for letter in word:
            print(letter)
        print ('You Won, the word was: %s'%word)
        tries=0

if tries == 0:
    if word not in guessed_word:
        print ('You Lose, the word was: %s'%word)

import random
words = ['ronaldo', 'kevin de bryune', 'lionel messi', 'romalu lukaku', 'trent',
'robertson', 'cancelo', 'antonio', 'salah']

correct_word = random.choice(words)



stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 6






display = []


for i in correct_word:
    display +=  "_"
print(display)

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter")
    guess_lower = guess.lower()

    word_length = len(correct_word)


    for i in range(word_length):
        
        if correct_word[i]== guess_lower:
            display[i] = guess_lower
            
    
    if guess_lower  not in correct_word:
        lives = lives-1
        if lives==0:
            end_of_game = True
            print("You lose")
      


    if "_" not in display: 
        end_of_game = True
        print("You Win")
    
    print(stages[lives])
    print("You guessed "+str(guess_lower)+" which is not in the word.You lose a life. You have 5 chances left to guess correctly")
        



    


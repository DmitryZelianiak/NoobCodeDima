import random
again = 'Y'
word_list = ['cool', 'best', 'home', 'car', 'good', 'think']
def get_word():
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = [ 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def game(word):
    guessed_letters = []
    guessed_words = []
    tries = 6
    play_word = len(word) * '_'
    guessed = False
    print('Let us play a Game!!!')
    print(display_hangman(tries))
    print(play_word)
    print()

    while guessed is False and tries > 0:
        given_answer = input('Tell me one letter or word!!!     ').upper()
        if len(given_answer) == 1 and given_answer.isalpha():
            if given_answer in guessed_letters:
                print('You told me already the letter!!!')
            elif given_answer not in word:
                print('There is no your letter in the word!!!')
                guessed_letters.append(given_answer)
                tries -= 1
            else:
                print('Good job!!, you found out a letter!!!')
            guessed_letters.append(given_answer)
            play_word_list = list(play_word)
            cutting = [i for i in range(len(word)) if word[i] == given_answer]
            for index in cutting:
                play_word_list[index] = given_answer
            play_word = ''.join(play_word_list) 
            if '_' not in play_word:
                guessed = True
        elif len(given_answer) == len(word) and given_answer.isalpha():
            if given_answer in guessed_words:
                print('You told already this word!!!')
            elif given_answer != word:
                print('You made a mistake!!!')
                tries -= 1
                guessed_words.append(given_answer)
            
            else:
                guessed = True
                play_word = word
        else:
            print('Tell me one more letter or a word!!!')
        print(display_hangman(tries))
        print(play_word)
        print()
    if guessed:
        print('You got it, You won the game!!!!')
        print(play_word)
    else:
        print(f'You lost, the word was:, {word}, good luck next time!!!!')


while again.lower() == 'y':
    word = get_word()
    game(word)
    again = input(' Would you like to play one more time?:  "Y or NO" ')

    

import random


def intro():
    name = input('Hello, What is your name my friend:   '   )
    int = f"Hey {name}, it's guessing game\n"
    int += 'You can pick out range of guessing numbers!\n'
    int += 'You are allowed to write only numbers\n'
    int += "At the end of the Game, i'll show you how many attemtps you did\n"
    int += 'Good luck'
    print(int)
    
    



def game():
    attempts = 0
    want_to_play = input('Do you wanna play my game?: "Yes" or "NO":   ')
    if want_to_play.lower() == 'yes':
         print("Let's go!!!!")
    else:
         print('Good luck!!!!')
         exit()
    intro()

    left, right = int(input('Tell me your min number?:   ')), int(input('Tell me your max number?:   '))
    while left >= right:
            print('You did it wrong!!!, one more time!!!')
            left, right = int(input('Tell me your min number?:   ')), int(input('Tell me your max number?:   '))

    random_number = random.randint(left, right)
        
    while want_to_play.lower() == 'yes':

        try:
             
             guess = int(input('Pick a number?:   '))
             if guess < left or guess > right:
                attempts += 1


                print('Give me a number within your range!!!')
                continue
             
             if guess == random_number:
                  print('You got it!!!!!')
                  print(f'Your attempts =  {attempts}')
                  game()
             if guess > random_number:
                  print('Nice shot, but too HOT')
                  attempts += 1
             elif guess < random_number:
                  print('Nice shot, but too COLD')
                  attempts += 1
        except ValueError:
             print('i need only numbers!!!!')
        except KeyError as err:
             print('Hey, not valid. One more time....')
             print('ERROR')
game()

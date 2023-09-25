import random
def start():
    answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
    promt = 'Hey Bro, I am magig ball, i cann answer any of your question'
    promt += '\nIf you do not have any questio say: NO'
    promt += '\nWhat is your name?:   '
    name = input(f'{promt}')
    print()
    print(f'Hello, my new player {name}')
    game(answers)
def game(answers):
    flag = True
    while flag == True:
        print('Ask me something, i will give you the answer!!!!')
        q_input = input()
        if not q_input == 'no'.lower():
            print(random.choice(answers))
            print('do you have any other questions?')
        else:
            print('Good luck, see you next time!!!')
            flag = False
start()







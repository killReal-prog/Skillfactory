import numpy as np

def game_core_v1(number):
    '''Используем алгоритм бинарного поиска для на нахождения
    загадaнного числа'''
    left = 1
    right = 101
    count = 1
    predict = 50
      
    while number!=predict:
        if number<predict:
            right-=int((right-left)/2)
        else:
            left+=int((right-left)/2)
        predict=int((right+left)/2)
        count+=1
    
    return(count)   
      
    
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v1)
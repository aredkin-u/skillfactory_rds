import numpy as np

def game_core_v3(number):
    '''реализуем алгоритм бинарного поиска'''
    count = 1
    start_int = 1
    end_int = 100
    # Для начала сделаем проверку на конец интервала
    predict = 100
    while number != predict and count < 100:

        # Если это не конец интервала, тогда начинаем бинарный поиск
        if count == 1:
            predict = 50

        count+=1
        if predict > number :
            end_int = predict
        elif predict < number:
            start_int = predict
        predict = (start_int+end_int)//2

    return(count) # выход из цикла, если угадали


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


# Проверяем
# score_game(game_core_v3)
#import pandas as pd
#pd.test()
#football = pd.read_csv('D:\Projects\skillfactory_rds\module_0\data_sf.csv')

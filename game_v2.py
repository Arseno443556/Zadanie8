"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    smoller_number = 1
    more_number = 100
    
    while True:
        mean = int((smoller_number+more_number)/2)   # находим среднее значение
        count += 1
        if mean == number:
            break 
        if mean < number:
            smoller_number = mean
        else:
            more_number = mean 
    return count      


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(random_predict)

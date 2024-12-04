import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = 64
    temp = 101
    while number != predict:
        count += 1
        if number > predict:
            predict = predict + (temp - predict)//2
        elif number < predict:
            temp = predict
            predict = predict//2
    #print(f'Текущее число {number}: количество попыток - {count}')
    return count

def max_attempt_score(game_core_v3) -> int:
    lst = []
    for number in range(1,101):  
        lst.append(game_core_v3(number))
    #print('Максимальное число попыток равно', max(lst))  
    return max(lst)

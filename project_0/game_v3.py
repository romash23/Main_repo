import numpy as np

def game_core_v3(number: int=1) -> int:
    """Сначала устанавливаем число 64, а потом делим его на 2, если искомое
    число меньше. Если же искомое число больше, тогда в качестве предсказания
    используем среднее между текущим предсказанием и верхней границей.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = 64 # Для удобства начимаем угадывать с 64, так как это степень 2-ки
    temp = 101 # Задаем верхнюю границу выборки, которую будем постепенно уменьшать
    
    while number != predict:
        count += 1
        
        if number > predict:
            # Берем среднее между предсказанием и верхней границей
            predict += (temp - predict)//2
            
        elif number < predict:
            temp = predict # Смещаем верхнюю границу влево
            predict //= 2 # Делим наше предсказание на 2
            
    return count

def max_attempt_score(game_core_v3) -> int:
    lst = []
    
    for number in range(0,101):  
        lst.append(game_core_v3(number))
    result = max(lst)    
    
    print(f"Максимальное число попыток равно {result}") 
    return result

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """'''реализуем алгоритм бинарного поиска'''
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    start_element = 1 
    end_element = 100
    count = 0
    found_num = 0
    
    # Условие выхода из цикла - нахождение числа или превышение количества попыток
    while number != found_num and count < 100:
        count+=1
        middle_element = start_element + (end_element - start_element) // 2
        if middle_element == number:
            found_num = middle_element
        elif middle_element < number:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
   
    return count # Возвращаем количество попыток
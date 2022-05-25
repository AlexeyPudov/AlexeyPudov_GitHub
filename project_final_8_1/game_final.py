import numpy as np

def random_predict(number:int=1)->int:
    """ Угадываем случайно загаданное число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number = 1
    max_number = 101
        
    while True:
        count += 1
        predict_number = int((min_number + max_number)/2) # предполагаемое число: среднее
                
        if predict_number > number:
            max_number = predict_number # отсекаем часть чисел сверху
            
        elif predict_number < number:
            min_number = predict_number # отсекаем часть чисел снизу
            
        else:
            break
    return count


def score_game(random_predict) -> int:
    """ Посчитаем среднее число попыток по угадыванию чмсла за 1000 экспериментов

    Args:
        random_predict (_type_): Функция угадывания случаного числа

    Returns:
        int: среднее за 1000 экспериментов число попыток
    """
    
    count_ls = [] # создаём список для сохранения количества попыток по каждому эксперименту
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # создаём список из 1000 чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # считаем среднее количество попыток
    
    print(f'Your algorithm guesses number in an average of {score} attempts')
    return score
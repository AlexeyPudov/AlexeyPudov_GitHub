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
        # Вводим редполагаемое число: берём среднее между двумя числами
        predict_number = int((min_number + max_number)/2)
        # Отсекаем часть чисел сверху
        if predict_number > number:
            max_number = predict_number
        # Отсекаем часть чисел снизу
        elif predict_number < number:
            min_number = predict_number
            
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
    
    # Создаём список для сохранения количества попыток по каждому эксперименту
    count_ls = []
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)
    # Создаём список из 1000 случайных чисел
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
     
    # Считаем среднее количество попыток
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses number in an average of {score} attempts')
    
    return score
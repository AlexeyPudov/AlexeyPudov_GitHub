""" Game (version 2).
Computer predictes and guesses number by itself.  
"""

from random import random
import numpy as np

def random_predict(number:int=1)->int: # program is guessing random number
    """ Guess random number

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        
        if predict_number == number:
            break
    return count
    


def score_game(random_predict) -> int:
    """ Calculate the average number of attempts out of 1000 experiments

    Args:
        random_predict (_type_): number guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = [] # list of attempt's number for every experiment
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000) # predicted array of random numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # calculate the average number of attempts
    
    print(f'Your algorithm guesses in an average of {score} attempts')
    return score

# RUN
if __name__=='__main__':
    score_game(random_predict)
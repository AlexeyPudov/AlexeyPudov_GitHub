import numpy as np

number = np.random.randint(1, 101) # program is guessing random number
count = 0 # number of attempts

while True:
    count += 1
    predict_number = int(input('Guess number from 1 to 100:'))
    
    if predict_number > number:
        print('Number should be less!')
        
    elif predict_number < number:
        print('Number should be greater!')
        
    else:
        print(f'You have guessed the number {number} for {count} attempts')
        break # finish program
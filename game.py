""" Игра 'Угадай число'
"""

from ast import While
from itertools import count

import numpy as np # импорт библиотеки NumPy
number = np.random.randint(1, 101) # загадываем число
count = 0 # счетчик попыток

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100'))
    
    if predict_number > number:
        print('Число должно быть меньше')
        
    elif predict_number < number:
        print('Число должно быть больше')
        
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break # конец игры, выход из цикла
        
        
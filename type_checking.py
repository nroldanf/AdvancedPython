'''
Docstring
'''
from typing import List, Tuple, Union
import random

def average(a: int, b: int, c: int) ->  float:
    '''
    This function returns the average.

    :param a: A number.
    :param b: A number.
    :paran c: A number.
    :return: Another number.
    '''
    return (a + b + c) / 3

def check_emptiness(lista_num: List[Union[int, str]]) -> bool:
    '''
    This function check if a list is empty. I know, it's useless.

    :param lista_num: List of numbers and strings.
    :return: If list is empty True.
    '''
    if len(lista_num) > 0:
        return False
    else:
        return True

def check_random() -> Tuple[str, int]:
    '''
    This function return if a random generated number is greater than 1.

    :return: A tuple with a string and int. The string is "Hey" if
    random number generated is greater than one, otherwise returns "Hi.
    The number is the random number generated.
    '''
    num_random: int
    sel: str
    num_random = random.choice(range(0, 20))
    if num_random > 1:
        sel = "Hey"
    else:
        sel = "Hi"
    return sel, num_random

print(average(1, 2, 3))
print(check_emptiness([1, "h", 3]))
print(check_random())

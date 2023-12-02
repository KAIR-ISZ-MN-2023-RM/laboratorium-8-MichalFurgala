import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle 
from inspect import isfunction


from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2 * x) + x ** 2 - 1

def dfun(x):
    return -2 * np.exp(-2 * x) + 2 * x

def ddfun(x):
    return 4 * np.exp(-2 * x) + 2

def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    # try:
    #     if not all(isinstance(a, (int, float)) and isinstance(b, (int, float)) and isfunction(f) and isinstance(epsilon, float) and isinstance(iteration, int)):
    #         raise TypeError
    #     if np.sign(f(a))==np.sign(f(b)):
    #         raise ValueError
    #     it = 0
    #     while it <= iteration:
    #         c = (a + b) / 2
    #         if np.abs(f(c)) < epsilon or np.abs(a-b) < epsilon:
    #             return c, it
    #         if np.sign(f(c)) == np.sign(f(a)):
    #             a = c
    #         else:
    #             b = c
    #         it += 1
                
    #         return c, iteration
        
    # except:
    #     return None
    
    
    
    if isinstance(a, (int,float)) and isinstance(b, (int, float)) and isinstance(epsilon, float) and isinstance(iteration, int):
        if np.sign(f(a)) != np.sign(f(b)):       

            it = 0
            while it <= iteration:
                c = (a + b) / 2
                if np.abs(f(c)) < epsilon or np.abs(a-b) < epsilon:
                    return c, it
                if np.sign(f(c)) == np.sign(f(a)):
                    a = c
                else:
                    b = c
                it += 1
                
            return c, iteration  
            
        else:
            return None
    else:
        return None
    


def difference_quotient(f: typing.Callable[[float], float],x: Union[int,float], h: Union[int,float]):
    '''Funkcja obliczająca iloaz różnicowy zadanej funkcji
    Parametry:
    
    f - funkcja dla której jest poszukiwane rozwiązanie
    x - argument funkcji la której jest 
    h - krok różnicy wykorzystywanej do wyliczenia ilorazu różnicowego
    
    return:
    diff - wartość ilorazu różnicowego
    
    '''
    if isinstance(x, (int, float)) and isinstance(h, (int, float)) and isfunction(f):
        pass
    else:
        return None
    
    return (f(x + h) - f(x)) / h

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[[float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if isfunction(f) and isfunction(df) and isfunction(ddf) and isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(epsilon, (float)) and isinstance(iteration, int):
        pass
    else:
        return None
    if np.sign(f(a)) != np.sign(f(b)):
        pass
    else:
        return None
    if np.sign(df(a)) == np.sign(df(b)):
        pass
    else:
        return None
    if np.sign(ddf(a)) == np.sign(ddf(b)):
        pass
    else:
        return None
    
    if f(a) * ddf(a) > 0:
        x = a
    else:
        x = b
    
    for i in range(iteration):
        xn  = x - f(x) / df(x)
        if np.abs(xn - x) < epsilon:
            return x, i
        x = xn
    return x, iteration

    
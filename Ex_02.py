from inputs import input_float
from math import sqrt

def square(size:float):
    return 4*size, size*size, sqrt(2*size*size)

size = input_float("Введите сторону квадрата: ")

print(square(size))

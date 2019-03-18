'''функция для построениия кривой коха'''

from turtle import *

def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

def main():
    up()
    goto(-100,0)
    down()
    n = int(input('Пожалуйста, укажите глубину рекурсии:'))
    a = int(input('Пожалуйста, укажите длину стороны:'))
    koch(n, a)

main()

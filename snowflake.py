'''Функция для построения снежинки коха'''

from turtle import *

def snezhinka(order, size):
    koch(order, size)
    right(120)
    koch(order, size)
    right(120)
    koch(order, size)


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
    snezhinka(n, a)

if __name__ == '__main__':
    main()

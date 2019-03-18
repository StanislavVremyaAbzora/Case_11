'''Функция для построения убегающего квадрата'''
from turtle import *

def k(d, n):
    if n == 0:
        return
    right(20)
    up()
    forward(d / 4)
    down()
    for x in range(4):
        forward(d)
        right(90)
    return k(0.8 * d, n -1)

def main():
     k(int(input('Пожалуйста, укажите глубину рекурсии:')),int(input('Пожалуйста, укажите длинну стороны:')))

if __name__ == '__main__':
    main()

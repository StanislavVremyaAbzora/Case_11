'''Функция для построение фрактала ветки'''

from turtle import *
def branch(n, size):
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)

    forward(x)
    left(180)
    forward(size)

def main():
    up()
    goto(0,-100)
    left(90)
    down()
    branch(int(input('Пожалуйста, укажите глубину рекурсии:')),int(input('Пожалуйста, укажите длину стороны:')))


if __name__ == '__main__':
    main()

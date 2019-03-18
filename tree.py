'''функция для построения двоичного дерева'''

from turtle import *

def tree(d, n):
    if n == 0:
        return
    forward(d)
    right(30)
    tree(d / 2, n - 1)
    left(60)
    tree(d / 2, n - 1)
    right(30)
    backward(d)

def main():
    left(90)
    d = int(input('Пожалуйста, укажите длину стороны'))
    n = int(input('Пожалуйста, укажите длину рекурсии'))
    tree(d,n)

if __name__ == '__main__':
    main()

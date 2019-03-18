'''Функция для построения кривой Минковского'''

from turtle import *
def mink(order, size):
    if order == 0:
      forward(size)
    else:
      mink(order-1, size/3) 
      left(90)
      mink(order-1, size/3)
      right(90)
      mink(order-1, size/3)
      right(90)
      mink(order-1, size/3*2)
      left(90)
      mink(order-1, size/3)
      left(90)
      mink(order-1, size/3)
      right(90)
      mink(order-1, size/3)
def main():
  up()
  goto(-100,0)
  down()
  n = int(input('Пожалуйста, укажите глубину рекурсии:'))
  a = int(input('Пожалуйста, укажите длину стороны:'))
  mink(n, a)

if __name__ == '__main__':
    main()

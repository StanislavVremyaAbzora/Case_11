'''Функция для построения ледяного фрактала 1'''

from turtle import *
def ice(order, size):
    if order == 0:
      forward(size)
    else:
      ice(order-1, size/2) 
      left(90)
      ice(order-1, size/3)
      right(180)
      ice(order-1, size/3)
      left(90)
      ice(order-1, size/2)
def main():
  up()
  goto(-100,0)
  down()
  ice((int(input('Пожалуйста, укажите глубину рекурсии:'))), (int(input('Пожалуйста, укажите длину стороны:'))))
main()

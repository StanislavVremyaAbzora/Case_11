'''Функция для построения кривой Леви'''

from turtle import *

def levi(order, size):
    if order == 0:          
        forward(size)
    
    else:
        levi(order-1, size/3)   
        right(90)
        levi(order-1, size/3)
        left(90)
        
        
def main():
    up()
    goto(-100,0)
    down()
    n = int(input('Пожалуйста, укажите глубину рекурсии:'))
    a = int(input('Пожалуйста, укажите длину стороны:'))
    levi(n, a)

if __name__ == '__main__':
    main()

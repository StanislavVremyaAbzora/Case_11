'''Функция для построения убегающего квадрата'''
import turtle

def k(d, n):
    if n == 0:
        return
    turtle.right(20)
    turtle.up()
    turtle.forward(d / 4)
    turtle.down()
    for x in range(4):
        turtle.forward(d)
        turtle.right(90)
    return k(0.8 * d, n -1)

def main():
     k(int(input('Пожалуйста, укажите глубину рекурсии:')),int(input('Пожалуйста, укажите длинну стороны:')))

if __name__ == '__main__':
    main()

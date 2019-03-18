def ice2(order, size):
    if order == 0:
      forward(size)
    else:
      ice2(order-1, size/2) 
      left(115)
      ice2(order-1, size/4)
      right(180)
      ice2(order-1, size/4)
      left(130)
      ice2(order-1, size/4)
      right(180)
      ice2(order-1, size/4)
      left(115)
      ice2(order-1, size/2) 
def main():
  up()
  goto(-100,0)
  down()
  n = int(input('Enter the depth of the recursion:'))
  a = int(input('Enter the side length:'))
  ice2(n, a)

if __name__ == '__main__':
    main()

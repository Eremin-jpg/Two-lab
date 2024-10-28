#coding=utf-8
def square(x):
  return x * x

def cube(x):
  return x * x * x

print("Значение может быть любым действительным числом")
x = float(input("Введите значение x: "))
print("Квадрат числа: {0:.5f}".format(square(x)))
print("Куб числа: {0:.5f}".format(cube(x)))
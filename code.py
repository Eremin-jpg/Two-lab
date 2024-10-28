#coding=utf-8
def square(x):
  return x * x

print("Значение может быть любым действительным числом")
x = float(input("Введите значение x: "))
print("Квадрат числа: {0:.5f}".format(square(x)))
from one import *
from kal import *
a = input("Введите строку: ")
print("Длинна строки:",str_len(a))
print("Развёрнутая строка:",str_inv(a))
print("Новая строка:", str_new(a))
b = input("Введите математический пример: ")
print("Ответ:", kal(b))
c = float(input("Введите число: "))
print("Корень", c,"равен:", sqrt(c))
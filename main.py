# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

# def text():
#     return print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\nBill Gates")
# text()


# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

# a = int(input())
# b = int(input())
# def num():
#     for i in range(a,b):
#       if i%2==0:
#          print(i)
# num()


# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

# def printSquere(lenght:int, simbol:str, fill:bool)->None:
#     l = lenght+2
#     s = ''
#     for x in range(l):
#       for y in range(l):
#         if x==0 or x==l-1:
#           if y==0:
#             s+= ' -'
#           elif y==l-1:
#             s+= ''
#           else:
#             s+= '--'
#         else:
#           if y==0 or y==l-1:
#             if y==0:  
#               s+= '|'
#             if y==l-1:
#               s+= ' |'
#           else:
#             if fill:        
#               s+= ' '+simbol
#             else:
#               s+= '  '
#       s+='\n'
#     print(s)
  
# l = int(input('Введите сторону квадрата'))
# s = input('Введите символ')
# z = bool(int(input('Закрашивать? (0,1)')))
# printSquere(l, s, z)  


# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

# def min_num(a,b,c,d,e):
#   return min(a,b,c,d,e)
# print(min_num(1,4,7,-3,2))



# Задание 5
# Напишите функцию, которая возвращает произве-
# дение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапа-
# зона перепутаны (например 5 верхняя граница, а 25
# нижняя граница), их нужно поменять местами.

# def product(a,b):
#   if a == b:
#     return 'Диапазон введён не верно' 
#   if a > b:
#     a,b == b,a 
#   c=1
#   for i in range (a,b+1):
#       c *= i
#   return c
# print(product(3,5))


# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4

# def m5_func_c1_t6(num):
#   num_str = str(num)
#   return len(num_str)
# print(m5_func_c1_t6(45365))


# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве пара-
# метра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.

# def palindrom(num):
#   num_str = str(num)
#   if num_str == num_str[::-1]:
#     return True
#   else:
#     return False
# print(palindrom(1233))
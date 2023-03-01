# strings

'''
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад: st = 'as 23 fdfdg544' введена строка 2,3,5,4,4 вивело в консолі.
'''

st = input()
numbers = []

for i in st:
    if i.isdigit():
        numbers.append(i)

print(','.join(numbers))

'''
2)написати прогу яка вибирає зі введеної строки числа і виводить їх
так як вони написані наприклад:  st = 'as 23 fdfdg544 34' #введена строка
23, 544, 34  #вивело в консолі
'''

st = input()
numbers = []

n = ''
for i in st:
    if i.isdigit():
        n += i
    else:
        if n.isdigit():
            numbers.append(n);
            n = ''
if n != '':
    numbers.append(n)

print(','.join(numbers))

# ist comprehension

'''1)є строка: greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']'''

greeting = 'Hello, world'
print(list(greeting.upper().strip()))

'''2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]'''

num = []
for i in range(51):
    if i % 2 != 0:
        num.append(i ** 2)

print(num)


# function

# - створити функцію яка виводить ліст
def print_list():
    print(list())


print_list()


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_num(n1, n2, n3):
    print(n1, n2, n3)
    max_n = n1
    if max_n < n2:
        max_n = n2
    if max_n < n3:
        max_n = n3
    return max_n


g = max_num(5, -898, 44);
print(g)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def max_min(*args):
    max_n = (args[0])
    min_n = (args[0])
    for i in args:
        if max_n < i:
            max_n = i
        if min_n > i:
            min_n = i
    print('max = %s' % max_n)
    return min_n


min_n = max_min(5, 9, 0, 1447, 9, 2, -8, 3)
print('min = %s' % min_n)


# - створити функцію яка повертає найбільше число з ліста
def max_in_list(lis):
    max_n = (lis[0])
    for i in lis:
        print(i)
        if max_n < i:
            max_n = i
    return max_n


# print('max in list = %s' %  max_in_list([9,6,3,7]))

# - створити функцію яка повертає найменьше число з ліста
def mim_in_list(lis):
    mim_n = (lis[0])
    for i in lis:
        if mim_n > i:
            mim_n = i
    return mim_n


# print('min in list = %s' %  mim_in_list([9,6,3,7]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_lis(lis):
    sum_l = 0
    for i in lis:
        sum_l = sum_l + i
    return sum_l


print('sum list = %s' % sum_lis([9, 6, 3, 7]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def mean_list(lis):
    mean_l = sum_lis(lis) / len(lis)
    return mean_l


print('mean list = %s' % mean_list([9, 6, 3, 7]))

'''
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
'''


def min_list(lis):
    return mim_in_list(lis)


def duplicates_list(lis):
    li = []
    [li.append(x) for x in lis if x not in li]
    return li


def x_list(lis):
    li = lis.copy()

    for i in range(3, len(li), 4):
        li[i] = 'X'
    return li


'''
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
'''


def square(side):
    for i in range(side):
        for j in range(side):
            if i == 0 or j == 0 or i == side - 1 or j == side - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


# square(10)


def multiplication_table():
    n = 1
    a = 1
    while n != 11:
        l = ''
        while a != 11:
            l = l + ' ' + str(n * a)
            a = a + 1
        print(l)
        n = n + 1
        a = 1


# multiplication_table()

my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def menu(n):
    while n != 6:
        if n == 4:
            square(10)
        elif n == 5:
            multiplication_table()
        elif n == 1:
            print(min_list(my_list))
        elif n == 2:
            print(duplicates_list(my_list))
        elif n == 3:
            print(x_list(my_list))

        print('1. Знайти min число в list')
        print('2. Видалити дублі в list')
        print('3. Замінити кожне 4 значення на Х в list')
        print('4. Квадрат із *')
        print('5. Таблиця множення')
        print('6. Вихід')

        n = int(input())


menu(0)
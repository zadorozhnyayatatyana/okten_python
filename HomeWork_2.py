"""1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи"""


def notebook():
    todo_list = []

    def add_todo(todo):
        todo_list.append(todo)
        get_all()

    def get_all():
        print(todo_list)

    return add_todo


"""
add = notebook()

add('todo 1')
add('todo 2')
add('todo 3')
"""

'''2) протипізувати перше завдання'''

from typing import Callable


def notebook() -> Callable:
    todo_list = []

    def add_todo(todo: str):
        todo_list.append(todo)
        get_all()

    def get_all():
        print(todo_list)

    return add_todo


add = notebook()

add('todo 1')
add('todo 2')
add('todo 3')

'''3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)'''


def expanded_form(numb: int) -> str:
    def order(n: int):
        return int('1' + '0' * (len(str(n)) - 1))

    lk = []
    current_numb = numb

    while current_numb != 0:
        number = order(current_numb)
        num = (current_numb // number) * number
        lk.append(str(num))
        current_numb = current_numb - num
    return ' + '.join(lk)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

'''4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, 
та буде виводити це значення після виконання функцій'''


def counter(func):
    count = 0

    def calc(*args, **kwargs):
        nonlocal count
        count += 1
        print('count: ', count)
        res = func(*args, **kwargs)
        print('----------------------------')
        return res

    return calc


@counter
def func1():
    print('func1')


@counter
def func2():
    print('func2')


func1()
func1()
func2()
func1()

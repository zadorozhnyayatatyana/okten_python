"""Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін"""
from abc import abstractmethod, ABC


class Rectangle:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f"{self.x, self.y}"

    def sqr(self):
        return self.x * self.y

    def __add__(self, other):
        return self.sqr() + other.sqr()

    def __sub__(self, other):
        return self.sqr() - other.sqr()

    def __eq__(self, other):
        return self.sqr() == other.sqr()

    def __ne__(self, other):
        return self.sqr() != other.sqr()

    def __lt__(self, other):
        return self.sqr() < other.sqr()

    def __gt__(self, other):
        return self.sqr() > other.sqr()

    def __len__(self):
        return self.x + self.y


rec1 = Rectangle(2, 2)
rec2 = Rectangle(4, 7)

print(len(rec1))
print(rec1 + rec2)
print(rec1 - rec2)
print(rec1 == rec2)
print(rec1 > rec2)
print(rec1 < rec2)

"""створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, 
та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення"""


class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f'{self.name, self.age}'


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        self.__class__.__count += 1

    @classmethod
    def get_count(cls):
        print(f'count = {cls.__count}')


class Prince(Human):

    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def find_her(self, girls):
        for girl in girls:
            if girl.foot_size == self.size:
                print(f"She is: {girl}")


cind1 = Cinderella('Liza', 20, 37)
cind2 = Cinderella('Irma', 19, 36)
cind3 = Cinderella('Kira', 18, 38)

Cinderella.get_count()

pr = Prince('Tom', 19, 36)
pr.find_her([cind1, cind2, cind3])

"""1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають 
є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу"""


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def print(self):
        print(f'{self.__dict__}')

    def __init__(self, name):
        self.name = name


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'{self.__dict__}')


class Main:
    __printable_list = []

    @classmethod
    def add(cls, some):
        if isinstance(some, Magazine) or isinstance(some, Book):
            cls.__printable_list.append(some)

    @staticmethod
    def show_all_magazines():
        for i in Main.__printable_list:
            if isinstance(i, Magazine):
                i.print()

    @staticmethod
    def show_all_books():
        for i in Main.__printable_list:
            if isinstance(i, Book):
                i.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

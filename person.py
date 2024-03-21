class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициация атрибутов человека - имя и возраст"""
        self.name = name  # используем self 
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):  # ������ �� ����� � ��������� ������, ���� ��� self
        """Просим человека станцевать"""
        print(self.name + " танцует")


man = Person("Alex", 30)  # в переменной man хранится значения класса Person
print(man.name)  # выведем имя человека (переменной)

man.dance()  # задействуем dance и ф-ция сама выводит на печать
woman = Person("Lila", 25)  # используя класс создаем женщину
woman.sing()
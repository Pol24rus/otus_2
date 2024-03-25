# from base_person import Person, Warrior
# from base_person import *  # импортироуем все классы из файла
#
# man = Person("Alex", 30, 180)
# man.description_person()
#
# warrior = Warrior("Konan", 32, 200)  # определили значения аттрибутов
# print("Ну Самого Нового человека зовут: " + warrior.description_person())  # при использовании return


import base_person  # импортируем всё, потм указываем откуда какой класс

man = base_person.Person("Alex", 30, 180)
man.description_person()
warrior = base_person.Warrior("Konan", 32, 200)  # определили значения аттрибутов
print("Ну Самого Нового человека зовут: " + warrior.description_person())  # при использовании return
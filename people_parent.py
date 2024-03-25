class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + " лет, его рост " + str(self.height) + ", его вес " + str(
            self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нового человека = " + str(self.weight) + " кг")

    """более правильный метод изменения веса для отдельного персонажа"""

    def update_weight(self, kg):
        """Изменение веса человека. Перезаписывает данные для get_weight"""
        self.weight = kg  # относится к новому методу, а не к основному методу


class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100  # добавили характеристику ярость, кроме имеющихся рост вес и тд
    """Метод для вывода отдельной (новой) характеристики"""

    def get_rage(self):
        """Получение ярости человека"""
        print("Ярость воина = " + str(self.rage) + " единиц")


warrior = Warrior("Konan", 32, 200)  # определили значения аттрибутов
warrior.update_weight(150)  # если хотим изменить вес, то надо ставить перед описанием
warrior.description_person()  # вызываем метод родительского класса, например описания
warrior.get_rage()

man = Person("Alex", 30, 180)
man.description_person()
# man.update_weight(110)  # здесь задаем значение веса
# man.get_weight()

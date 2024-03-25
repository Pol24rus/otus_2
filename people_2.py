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


man = Person("Alex", 30, 180)
man.update_weight(110)  # здесь задаем значение веса
man.get_weight()

class Person():
    """Создаем человека"""

    def __init__(self, name, age, height, weight):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + " лет, его рост " + str(self.height) + ", его вес " + str(
            self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        print("Вес нового человека = " + str(self.weight) + " кг")


man = Person("Alex", 30, 180, 100)
man.description_person()
man.get_weight()
"""Если в стр. 9 задать значение (100) и в 4-й стр убрать weight, то у всех экземпляров в данном классе вес будет 100 
кг, тк задан. В строке 21 тоже нужно убрать вес"""
"""чтобы изменить вес у человека (у экземпляра класса, но не у всего класса) то в стр 23 надо прописать man.weight = 
110. Все остальные экземпляры класса будут иметь значение по умолчанию = 100"""

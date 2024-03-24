class Cat():
    """Создаем кошака"""

    def __init__(self, name, color, age):
        """Инициируем нового кошака с заданными параметрами"""
        self.name = name
        self.color = color
        self.age = age

    def get_description_cat(self):
        """Получим описание нашего вновь созданного котяры"""
        print(f"Котяру звать {self.name}, ему пока {self.age} месяцев и он имеет {self.color} цвет")

    def update_age(self, new_age):
        """Котяра вырос и у него изменился возраст"""
        self.age = new_age


cat_1 = Cat("Шейн", "белый", 8)
cat_1.get_description_cat()
cat_1.update_age(9)
cat_1.get_description_cat()
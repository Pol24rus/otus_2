class Car():
    def __init__(self):  # лучше этот вариант, короче данная строка и код, чем строка 3
        # def __init__(self, model, year, volume, price, odometr, wheel):
        # self.model = model
        # self.year = year
        # self.volume = volume
        # self.price = price
        # self.odometr = odometr
        # self.wheel = wheel

        self.model = "ВАЗ"
        self.year = 2001
        self.volume = 1.3
        self.price = 50000
        self.odometr = 250000
        self.wheel = 4

    def car_info(self):  # информация по объекту
        infocar = (
                "Модель - " + self.model + ", год выпуска - " + str(self.year) + ", Объём двигателя - "
                + str(self.volume) + " л., пробег - " + str(self.odometr) + ", цена = " + str(self.price) +
                ", кол-во колес - " + str(self.wheel))
        return infocar


class Lorry(Car):  # наследник грузовик, но меняю кол-во колес
    def __init__(self):
        super().__init__()
        self.wheel = 8


# car = Car("ВАЗ", 2001, 1.3, 50000, 250000, 4)  # вариант если использовать строки 3-9, но сложнее код
car = Car()
lorry = Lorry()
avto = input("Какой автомобиль выбираете, легковой (введите 1) или грузовой (введите 2)? ")
try:
    if avto == "1":
        a = str(car.car_info())
        b = "легковой"
    elif avto == "2":
        a = str(lorry.car_info())
        b = "грузовой"
    else:
        a = "Введите 1 или 2 а не вот это вот всё"
        b = "выбрать"
except Exception:  # любая возможная ошибка
    a = 0

print(f"Предлагаем {b} автомобиль: {a}")

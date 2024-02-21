# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

# # функция с переменными внешними str 12-21
# num_1 = 10
# num_2 = 20
#
#
# def summ():
#     result = num_1 + num_2
#     print(result)


# summ()

# функция с переменными прописываемыми в самой ф-ции
def summ(num_1, num_2):
    result = num_1 + num_2
    print(result)


summ(10, 20)
summ(30, 40)
summ("Hello ", "world")
summ(num_2="world ", num_1="Hello ")  # прописать переменные и самим определить их порядок


def hi(name):
    print("Hello" + name)


hi("Alex")


def hi(name="Alex"):  # то же самое, только значение присваивается переменной в начале ф-ции
    print("Hello " + name)


hi()

name = "Alex"


def hi(name):  # аргумент name указан как обязательный
    print("Hello" + name)


hi(name)

name = "Alex"


def hi(name, age):
    print("Hello " + name + " I'm " + age + " years old")


hi(name, "32")

# используем input
name = input("Введи имя ")


def hi(name, age):
    print("Hello " + name + " I'm " + age + " years old")


hi(name, "53")


# тут осуществляется возврат
name = "Alex"
age = "53"
def hi(name, age):
    result = name + " " + age
    return result


h = hi(name, "32")
print(h)
print(hi(name, "32"))  # то же самое, но громоздкое

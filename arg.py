# как присваиваются значения в ф-циях

# def description(name, age, sex):
#     print(f"Имя {name}, Возраст {age}, пол {sex}")
#
#
# # description("Anna", 30, "woman")  # позиционный аргумент
# description(name="Anna", age=30, sex="woman")  # именованный аргумент, можно в любом порядке


n = "Anna"
m = 30


def description(name, age, sex):
    print(f"Имя {name}, Возраст {age}, пол {sex}")


description(n, m, "woman")

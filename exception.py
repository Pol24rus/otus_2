a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))

# добавим условие что на ноль делить нельзя
# try:
#     result = int(a / b)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# print("Результат = ", result)

# но чтобы не выдавалась ошибка, присвоим переменной значение
try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("На ноль делить нельзя")
print("Результат = ", result)

# для проверки что будет без ошибки, сделаем ещё один пример
result_2 = a + b
print("Сумма = ", result_2)
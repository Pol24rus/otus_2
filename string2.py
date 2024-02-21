str_1 = "hello"
str_2 = "WORLD"
print(str_1)
print(dir(str_1))  # dir показывает все действия, возможные с переменной
print(str_1.upper())  # точка после переменной позволяет добавить действие
print(str_1.title())
print(str_2)
print(str_2.lower())

name = "Ivan"
a = "Yello {}"
result = a.format(name)
print(result)

first_name = "Ivan"
last_name = "Petrov"
a = '{} {}'
result = a.format(first_name, last_name)
print("My name is: " + result)

result = f'{first_name} {last_name}'  # данн ф-ция вместо стр. 17 и 18 дает одну стр
print("My name is: " + result)
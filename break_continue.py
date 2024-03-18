# list = [1, 2, 4, 6, 10]
#
# for i in list:
#     if i == 6:
#         print("6 is all correct")
#         break
#     print(i)

# login = input("Введите логин: ")
#
# while True:
#     if login =="Alex":
#         print("Вы ввели верный логин")
#         password = input("Введите пароль: ")
#
#     else:
#         print("Логин некорректный")
#         break


list = [1, 2, 4, 6, 8, 10, 12]

for i in list:
    if i == 10:
        print("Плохо 10")
        break

    elif i == 2:
        print("Ура 2")

    elif i == 6:
        print("Ура 6")
        continue

    print(i)
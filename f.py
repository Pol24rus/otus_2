# age = 25
# name = "Pol"
# if age == 25 or name == "Pol":
#     print("I'm 25 years old and i'm Pol")
# # elif age > 25:
# #     print("I'm older than 25 years")
# else:
#     print("I'm younger 25 years old")

# name = "Pol"
# if "f" in name:
#     print("My name is Pol")
# else:
#     print("Вы ошиблись")

pin = 1234
user_pin = int(input("Введите пин-код: ", ))
if pin == user_pin:
    print("Совпадение")
else:
    print("Мимо кассы, ещё две попытки")
    user_pin = int(input("Введите пин-код: ", ))
    if pin == user_pin:
        print("Совпадение")
    else:
        print("Мимо кассы, ещё один попытки")
        user_pin = int(input("Введите пин-код: ", ))
        if pin == user_pin:
            print("Совпадение")
        else:
            print("Мимо кассы, давай досвидания")

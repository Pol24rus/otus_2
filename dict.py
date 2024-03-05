# список
family_1 = ["Alex", "Olga", "Semen", "Nastya", "Alex"]
print(family_1)

# множество
family_2 = {"Alex", "Olga", "Semen", "Nastya", "Alex"}
print(family_2)
family_2_1 = {"Alex", "Olga", "Semen", "Nastya", "alex"}
print(family_2_1)

# словарь (ключ: значение)
family_3 = {"Папа": "Alex", "Мама": "Olga", "Брат": "Semen", "Дочь": "Nastya"}
print(family_3["Папа"])
for k, v in family_3.items():  # items обозначает элементы
    print(k)  # печатаем k - key ключ
    print(v)  # печатаем v - variable значение
    print(k, v)
    print(k + "-" + v)

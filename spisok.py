personal = ["Alex", "Ivan", "Nasty", "Olga"]
result = personal[0] + " + " + personal[2]
# print(result + " = best friend's")
# print(personal[1])
number = [1, 15, 23, 4]
print(number[2])
result_num = number[1] + number[3]
print(result_num)

print("длина списка = ", len(personal)) # длина списка, кол-во элементов в списке
print("последний элемент списка - ", personal[-1]) # последний элемент в списке
print("первые 2 элемента списка - ", personal[0:2]) # первые 2 элемента, 0 и 1. сама 2 не входит
print("все значения со 2-го элемента - ", personal[1:])
personal.append("Fedor") # Добавляем в список сотрудника
print("Добавленный список: ", personal)

pn = []
pn.append(personal) # список personal + number
pn.append(number)
print("совмещенные списки - ", pn)
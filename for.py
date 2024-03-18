students = ["Alex", "Ivan", "Nasty", "Olga", "Semen", "Igor", "Svetlana"]
print(students)

for f in students:
    var = "Engeener " + f
    print(var)

for f in students:
    if f == "Olga":
        print("Only Olga - ", f)
        var = "Engeener " + f
        print(var)

for f in students[:3]:
    print("Первые три в списке - ", f)

for f in students:
    print("кол-во символов в именах: ", len(f))
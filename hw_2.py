a = int(input("Введите число номер один: "))
b = int(input("Введите число номер два: "))
c = input("Что вы хотите сделать - разделить (введите '/'), умножить (введите '*'), сложить (введите '+') или отнять "
          "(введите '-') ?: ")

if c == "/":
    result = int(a / b)
elif c == "*":
    result = int(a * b)
elif c == "+":
    result = int(a+b)
elif c == "-":
    result = int(a - b)

# print(result)
print("Результат : " + str(result))
# try:
#
# except: ZeroDivisionError:
#     print("На ноль делить нельзя")

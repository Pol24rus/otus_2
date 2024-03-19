try:
    a = int(input("Введите число номер один: "))
    c = input("Что вы хотите сделать - разделить (введите '/' или 'р')"
              " умножить ('*' или 'у'), сложить ('+' или 'с') или отнять (разница) ('-' или 'в') ?: ")
    b = int(input("Введите число номер два: "))
except ValueError:
    # except TypeError:
    a = "Введенные данные 1"
    b = "Введенные данные 2"
    # res_2 = "��������� �������� � ������ � �������"
    # result = "Ошибка"
    print("совершить действие с числом и строкой")


try:
    if c == "/" or c == "р":
        result = (a / b)
        res_2 = "деление"
    elif c == "*" or c == "у":
        result = int(a * b)
        res_2 = "умножение"
    elif c == "-" :
        result = int(a - b)
        res_2 = "вычитание"
    elif c == "+" or c == "с":
        result = int(a + b)
        res_2 = "сложение"
    else:
        result = "Ошибка"
        res_2 = "действие с неправильным оператором"
        # print("Что то тут неправильно")

except ZeroDivisionError:
    result = "Ошибка"
    res_2 = "разделить на ноль"
# #
except UnicodeEncodeError:
    # d = (c)
    print(f"Введите правильно действие вместо {b}")
except Exception:
    res_2 = "совершить неверное действие"
    result = "Ошибка"
else:
    c = 0
    # print('Все хорошо.')

print(f"С числами {a} и {b} вы хотели выполнить {res_2}, результат = {result}")

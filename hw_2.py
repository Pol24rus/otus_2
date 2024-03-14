a = int(input("Введите число номер один: "))
b = int(input("Введите число номер два: "))
c = input(
    "Что вы хотите сделать - разделить (здесь и далее введите '/' или 'д'), умножить ('*' или 'у'), сложить ('+' или "
    "'с') или отнять ('-' или 'р') ?: ")

try:
    if c == "/" or c == "д":
        result = (a / b)
        res_2 = "деление"
    elif c == "*" or c == "у":
        result = int(a * b)
        res_2 = "умножение"
    elif c == "+" or c == "с":
        result = int(a + b)
        res_2 = "сложение"
    elif c == "-" or "р":
        result = int(a - b)
        res_2 = "вычитание"
except ZeroDivisionError:
    result = "Ошибка"
    res_2 = "разделить на ноль"
# #
except ValueError:
    # except TypeError:
    res_2 = "совершить действие с числом и строкой"
    result = "Ошибка"

except Exception:
    res_2 = "совершить неверное действие"
    result = "Ошибка"
else:
    print('Всё хорошо.')

print(f"С числами {a} и {b} вы решили выполнить {res_2}, результат = {result}")

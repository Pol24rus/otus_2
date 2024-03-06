import hello
# import math  # ф-ция математик всяких
import random  # ф-ция случайных чисел

# hello.some()  # импортировали файл с ф-цией и запустили её
# print(math.pi)  # число Пи
r = random.randrange(0, 10)  # аналог range
user = "User "
print(user + str(r))
# а лучше сделать так:
user_random = user + str(r)
print(user_random)
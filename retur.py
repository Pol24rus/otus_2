# # def identification(name):
# #     print("Вы являетесь ")
# #
# #     if name == "Alex":
# #         print("преподавателем")
# #     else:
# #         print("студентом")
# #
# #
# # name = input("Введите ваше имя: ")
# # identification(name)
#
# def identification(name):
#     print("Вы являетесь ")
#
#     if name == "Alex":
#         result = "Автором"
#         # print("преподавателем")
#     else:
#         result = "Студентом"
#         # print("студентом")
#
#     return result
#
#
# # name = input("Введите ваше имя: ")
# # print(identification(name))
#
# name = input("Введите ваше имя: ")
# n = "Alex "
# s = identification(name)
# print(n + s)

def identification(name):
    print("Вы являетесь ")

    if name == "Alex":
        result = "Автором"
        # print("преподавателем")
    else:
        result = "Студентом"
        # print("студентом")

    return result


def status(result):
    print(result)


name = input("Введите ваше имя: ")

status(identification(name))

# for i in range(5):
#     doc_file = open('doc/file.txt', 'a')
#     doc_file.write("Это есть тестовая строка N" + str(i + 1) + "\n")
#     doc_file.close()
#
# doc_file = open('doc/file.txt', 'r')
# text = doc_file.read()
# doc_file.close()
#
# print(text)

var = input("Введите число: ")  # запись новых данных в конец файла
f2 = open('doc/file1.txt', 'a')
f2.write(var + '\n')
text1 = f2.read()
f2.close()


# fr1 = open('doc/file1.txt')  # чтение и печать данных записанных в файле 1
# text1 = fr1.read()
# fr1.close()
print(text1)
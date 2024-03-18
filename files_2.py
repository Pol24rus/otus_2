# for i in range(5):
#     doc_file = open('doc/file.txt', 'a')
#     doc_file.write("Это b есть тестовая строка N" + str(i + 1) + "\n")
#     doc_file.close()
#
# doc_file = open('doc/file.txt', 'r')
# text = doc_file.read()
# doc_file.close()

f1 = open('doc/file1.txt', 'a')  # запись новых данных в конец файла
f1.write("Hello world\n")
f1.close()

var = input("Введите число: ")  # запись новых данных в конец файла
f2 = open('doc/file1.txt', 'a')
f2.write(var + '\n')
f2.close()

f3 = open('doc/file2.txt', 'r+')  # чтение и перезапись того что было во 2-м файле
f3.write(var)
f3.close()
print(var)

# fr1 = open('doc/file1.txt', 'r')
# fr2 = open('doc/file2.txt', 'r')
# text1 = fr1.read()
# text2 = fr2.read()
# fr1.close()
# fr2.close()
# print(text1 + text2)
# # print(text2)

fr1 = open('doc/file1.txt')  # чтение и печать данных записанных в файле 1
text1 = fr1.read()
fr1.close()
print(text1)
# fr1 = open('doc/file2.txt', 'r')
# text1 = fr1.read()
# fr1.close()
# print(text1)

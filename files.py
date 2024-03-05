# var = input("Напиши что-нибудь: ")
# fw = open('dir/file.txt', 'a')
# fw.write(var)
# fw.close()

# a - запись новых данных в файл и помещение их в конец файла
# w - запись новых данных с удалением старых

# fw = open('dir/file_2.txt', 'w')
# fw.write("Privet!!!")
# fw.close()

fr = open('dir/file.txt', 'r')
fr_2 = open('dir/file_2.txt', 'r')
text = fr.read()
text_2 = fr_2.read()
fr.close()

print(text)
print(text_2)
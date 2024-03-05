file_name = "dir/file_3.txt"
data = "Hello world 2"

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'a') as fw:  # с with не надо закрывать файл, сохраняем как fw
    fw.write(data + '\n')  # записываем данные и вставляем перенос

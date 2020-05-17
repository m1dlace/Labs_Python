#Напишите скрипт, позволяющий искать в заданной директории и в
#ее подпапках файлы-дубликаты на основе сравнения контрольных
#сумм (MD5). Файлы могут иметь одинаковое содержимое, но
#отличаться именами. Скрипт должен вывести группы имен
#обнаруженных файлов-дубликатов.

import string
import os
import hashlib

path = 'E:\\Хлам\\Мэмы'
files = os.listdir(path)
filecount = []
for file in files:
    with open(path+'\\'+file, 'rb') as f:
        content = f.read()
        f.close()
        filecount.append(hashlib.md5(content).hexdigest())

for i in range(len(files) - 1):
    for j in range(i + 1, len(files)):
        if filecount[i] == filecount[j]:
            print(files[i], ' is ', files[j])


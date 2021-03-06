﻿#Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла,
#найти в нем с помощью регулярных выражений все подстроки определенного вида,
#в соответствии с вариантом. Например, для варианта № 1 скрипт должен вывести
#на экран следующее:
# Строка 3, позиция 10 : найдено '11-05-2014' 
# Строка 12, позиция 2 : найдено '23-11-2014' 
# Строка 12, позиция 17 : найдено '23-11-2014' 



#Вариант 5: Найты все номера типа (000)1234567.
#Вар5

import string
import os
import hashlib
from glob import glob
import os.path
import re

def search_pattern(line_in_file):
    pattern = re.compile("[(]\d{3}[)]\d{7}")
    counter = 0
    for line in line_in_file:
        counter += 1
        time = re.findall(pattern, line)
        if time:
            for new_time in time:
                print('Строка {0}, позиция {1} : найдено {2}'.format(counter, line.index(new_time), new_time))
    return

file_name = input("Введите существующий файл - 'Text.txt': ")

try:
    file_loaded = open(file_name)
    lines_in_file = file_loaded.readlines()
    search_pattern(lines_in_file)
except Exception:
    print('Такого файла нет!')
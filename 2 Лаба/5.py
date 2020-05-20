#Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все
#слова, которые начинаются с большого латинского символа (от A до Z) и заканчиваются
#2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002».
#Используйте регулярные выражения.

import string
import os
import hashlib
from glob import glob
import os.path
import re

text = input("Введите текст: ")
pattern = r'[A-Z]\D+\d{2}\b'
pattern2 = r'[A-Z]\D+\d{4}\b'
list_words = re.findall(pattern, text)
list_words2 = re.findall(pattern2, text)

for i in range(len(list_words)):
    print(list_words[i])

for i in range(len(list_words2)):
    print(list_words2[i])
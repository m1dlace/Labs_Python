#Задан путь к директории с музыкальными файлами
#(в названии которых нет номеров, а только названия песен)
#и текстовый файл, хранящий полный список песен с номерами
#и названиями в виде строк формата «01. Freefall [6:12]».
#Напишите скрипт, который корректирует имена файлов в директории
#на основе текста списка песен.

import string
import os
import hashlib
from glob import glob
import os.path
import re

music_list = {}
path = os.getcwd() + "\\Music"
number = r'(\d+\.\s)[\w\s-]+'
name = r'\d+\.\s([\w\s-]+)'

f = open ('Desktop/Music/MList.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    name =''.join(re.findall(name, line)).rstrip()
    num = ''.join(re.findall(number, line))
    music_list[name] = num

    
for name in os.listdir(path):
    if name.endswith('.mp3') and name[:-4] in music_list:
        os.rename(path + "\\" + name, path + "\\" + music_list[name[:-4]] + name)
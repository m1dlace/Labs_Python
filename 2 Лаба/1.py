#Напишите скрипт, который читает текстовый файл и
#выводит символы в порядке убывания частоты встречаемости
#в тексте. Регистр символа не имеет значения. Программа
#должна учитывать только буквенные символы (символы
#пунктуации, цифры и служебные символы слудет игнорировать).
#Проверьте работу скрипта на нескольких файлах с текстом на
#английском и русском языках, сравните результаты с таблицами,
#приведенными в wikipedia.org/wiki/Letter_frequencies.


import string

file = open('Desktop/file.txt', 'r') 
text = file.read()
file.close()
q = '!@#№$%^&*(),.:;?/|"[]+_-'

Bukv = {letter: text.count(letter) for letter in text if letter not in q}
for key in sorted(Bukv.keys(), key=Bukv.get, reverse=True):
    print(key, ': ', Bukv[key])
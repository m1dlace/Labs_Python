﻿-----------------------------------111111111111------------------------------------------
try:
	k = float(input('Введите число: ')) 
	monet = (k - int(k)) * 100 
	assert k > 0 
	print(int(k),' руб.', int(monet), ' коп.')
except AssertionError :
	print('Введите положительное число!')

------------------------------------22222222222------------------------------------------

Numb = input('Введите цифры: ').split(' ')
print(True) if [i for i in range(len(Numb)-1) if Numb[i] <= Numb[i+1]] else print(False)

------------------------------------33333333333------------------------------------------

DC = input('Введите номер карты: ').replace(' ', '').replace('-', '')
print(DC[:4] + '********' + DC[12:16]) if len(DC) == 16 else print("Это не номер карты!")

------------------------------------44444444444------------------------------------------

Lol = input('Введите текст: ').split(' ')
print('> 7: {0}\n'.format([i for i in Lol if len(i) > 7]))
print('4 - 7: {0}\n'.format([i for i in Lol if len(i) >= 4 and len(i) <= 7]))
print('<= 4: {0}\n'.format([i for i in Lol if len(i) < 4]))

------------------------------------555555555555------------------------------------------

Lol = input('Введите текст: ').split(' ')
print(' '.join([n.upper() if n == n.title() else n for n in Lol]))

------------------------------------666666666666------------------------------------------

Lol = input()
print('Символы по 1 разу:', ', '.join([i for i in Lol if Lol.count(i) == 1]))

------------------------------------777777777777------------------------------------------

site = input("Введите сайты: ").split(' ')
Adon = ['http://' + i if ('www.' in i) else '' + i for i in site]
print([i + '.com' if (not '.com' in i) else i for i in Adon])

------------------------------------888888888888------------------------------------------

import random
import math
ar = [int(random.uniform(1, 1000)) for i in range(0, int(random.uniform(1, 10000)))]
n = 2 ** math.ceil(math.log2(len(ar)))
print('После: {0}\n'.format(len(ar)))
[ar.append(random.uniform(1, 1000)) for i in range(len(ar), n)]
print('После: {0}\n'.format(len(ar)))
 
------------------------------------99999999999------------------------------------------

bank_m = [5000, 1000, 500, 200, 100, 50, 10]
bank_k = [10, 10, 15, 15, 20, 20, 30]
bank_k2 = [10, 10, 15, 15, 20, 20, 30]
Sum = 0
a = int(input("Введите кол-во Money: "))
for i in range(len(bank_m)):
  Sum += bank_m[i]*bank_k[i]
if a <= Sum:
    for i in range(len(bank_m)):
      while  a >= bank_m[i]:
        a -= bank_m[i]
        bank_k[i] -= 1
    for i in range(len(bank_m)):
      print(bank_m[i], "*", bank_k2[i]-bank_k[i])
else:
    print("В банке не достаточно средств!")

------------------------------------101010101010------------------------------------------

import re

Pas = str(input('Введите пароль: '))
L = 0;
if len(Pas) > 6 and len(Pas) < 9:
  L += 10
if len(Pas) > 9 and len(Pas) < 12:
  L += 15
if len(Pas) > 12 and len(Pas) <= 16:
  L += 20
if len(Pas) > 16:
  L += 25
if Pas.isalpha() == False:
  L += 5
if Pas.isdigit() == False:
  L += 5
if Pas.isascii() == False:
  L += 5
if Pas.islower() == False:
  L += 5
if Pas.isupper() == False:
  L += 5
if re.search('[{}@#$%^&+=*()?!.,~]', Pas):
  L += 10
for i in range(len(Pas)-1):
  if Pas[i] != Pas[i+1]:
    L += 1
for i in range(len(Pas)-1):
  if Pas[i].isdigit() != Pas[i+1].isdigit():
    L += 0.5
  if Pas[i].isalpha() != Pas[i+1].isalpha():
    L += 0.5
if "123456" or "56789" or "qwerty" in Pas:
  L -= 15
if Pas == '123456' or Pas == "qwerty":
  L = 0
if len(Pas) <= 4:
  L -= 5
print('Сложность паоля = ', L, '%')

------------------------------------111111111111------------------------------------------

def frange(X, Y, Z):
    while X <= (Y - Z):   
      yield float('{:.1f}'.format(X + Z))   
      X = X + Z

for x in frange(1, 5, 0.1):
  print(x)

------------------------------------121212121212------------------------------------------

def get_frames(signal, size, overlap):
    Ln = int(size*overlap)
    Step = 0
    while Step < len(signal) - 1:
        yield signal[Step: Step + size]
        Step =  Step + Ln

try:
  Vvod = int(input('Введите блину сигнала ( 0 - 10 ): '))
  signal = [i for i in range(Vvod)]
  for frame in get_frames(signal, 10, 0.5):
    print(frame)

except ValueError:
  print('ERROR! Некорректрый формат!')

------------------------------------131313131313------------------------------------------

def extra_enumerate(x):
    temp = 0
    for i in x:
        temp += i
        yield i, temp, temp/sum(x)

x = [1, 3, 4, 2]
for elem, summ, frac in extra_enumerate(x):
  print(elem, summ, frac)

------------------------------------141414141414------------------------------------------

def non_empty(listRetFunction):
    def wrapper():
        returned = listRetFunction()
        deleted = 0
        for i in returned:
            if i is None or i == '':
                returned.pop(deleted)
            deleted += 1
        return returned
    return  wrapper

@non_empty
def getList():
    return ['chapter1', '', 'contents', '', 'line1']

print(getList())

------------------------------------151515151515------------------------------------------

def pre_process(a):
    def Decorator(listRetFunction):
        def wrapper(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] = s[i]-a*s[i-1]
                print('a = ', a)
                listRetFunction(s)
        return  wrapper
    return Decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

signal = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
plot_signal(signal)

------------------------------------161616161616------------------------------------------

import datetime
import random

List = [
    'Шахтер', 'Динамо', 'Спартак', 'Челси',
    'Реал Мадрид', 'Ювентус', 'Реал Харцызск', 'Ливерпуль',
    'Мадрид', 'ФК Рубин', 'ЕСК', 'Арсенал',
    'Рональдо', 'Казантип', 'Россия', 'Еще что-то'
]
Date = datetime.datetime(2020, 9, 14, 22, 45)
random.shuffle(List)
paty = [List[i*4:i*4+4] for i in range(4)]
[print('Матчи #:', i+1, ' - ', paty[i]) for i in range(len(paty))]

for i in range(len(List)):
  print("Матчи #:", i, Date.strftime("%d/%m/%Y %H:%M"))
  Date += datetime.timedelta(days=14)
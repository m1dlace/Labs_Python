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
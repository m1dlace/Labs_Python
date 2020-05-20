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
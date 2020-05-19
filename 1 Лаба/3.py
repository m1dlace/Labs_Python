DC = input('Введите номер карты: ').replace(' ', '').replace('-', '')
print(DC[:4] + '********' + DC[12:16]) if len(DC) == 16 else print("Это не номер карты!")
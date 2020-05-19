Lol = input('Введите текст: ').split(' ')
print(' '.join([n.upper() if n == n.title() else n for n in Lol]))
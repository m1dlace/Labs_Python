site = input("Введите сайты: ").split(' ')
Adon = ['http://' + i if ('www.' in i) else '' + i for i in site]
print([i + '.com' if (not '.com' in i) else i for i in Adon])
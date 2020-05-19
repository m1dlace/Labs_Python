Lol = input('Введите текст: ').split(' ')
print('> 7: {0}\n'.format([i for i in Lol if len(i) > 7]))
print('4 - 7: {0}\n'.format([i for i in Lol if len(i) >= 4 and len(i) <= 7]))
print('<= 4: {0}\n'.format([i for i in Lol if len(i) < 4]))
Numb = input('Введите цифры: ').split(' ')
print(True) if [i for i in range(len(Numb)-1) if Numb[i] <= Numb[i+1]] else print(False)
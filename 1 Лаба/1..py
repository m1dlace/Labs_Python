try:
	k = float(input('Введите число: ')) 
	monet = (k - int(k)) * 100 
	assert k > 0 
	print(int(k),' руб.', int(monet), ' коп.')
except AssertionError :
	print('Введите положительное число!')

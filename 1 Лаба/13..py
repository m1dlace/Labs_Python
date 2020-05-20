def extra_enumerate(x):
    temp = 0
    for i in x:
        temp += i
        yield i, temp, temp/sum(x)

x = [1, 3, 4, 2]
for elem, summ, frac in extra_enumerate(x):
  print(elem, summ, frac)
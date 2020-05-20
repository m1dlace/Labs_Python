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
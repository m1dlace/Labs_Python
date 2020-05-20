def frange(X, Y, Z):
    while X <= (Y - Z):   
      yield float('{:.1f}'.format(X + Z))   
      X = X + Z

for x in frange(1, 5, 0.1):
  print(x)
def pre_process(a):
    def Decorator(listRetFunction):
        def wrapper(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] = s[i]-a*s[i-1]
                print('a = ', a)
                listRetFunction(s)
        return  wrapper
    return Decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

signal = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
plot_signal(signal)

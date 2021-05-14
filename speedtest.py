import time

def method1():
    for i in range(0,1000000):
        var = i
def method2():
    var = 0
    for i in range(0,1000000):
        var += 1
def Average(arr): 
    avg = sum(arr) / len(arr) 
    return avg



times = []
for i in range(0,10):
    time_start = time.time()
    method2()
    time_end = time.time()
    times.append(time_end-time_start)
print(Average(times))

#vysledek, prirazovani je rychlejsi





import math
import time

for k in range(10000):
    time1=time.time()
    print("Zahl=",k, "doppelte Zahl:", k*2, "quadrat:",k**2, "hoch 3:",k**3)
    print("Fakultät:", math.factorial(k))
    time2=time.time()
    print("berechnungsdauer:",time2-time1)
    print("")


import math

def primechecker(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1


sum_primes=2
for i in range(3,2000000,2):
    a=primechecker(i)
    if a==1:
        sum_primes+=i
print("Sum:",sum_primes) 

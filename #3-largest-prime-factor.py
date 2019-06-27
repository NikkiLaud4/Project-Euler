import math
candidate=[]
def primechecker(f):
    count=0
    for i in range(2,int(math.sqrt(f))+1):
        if f%i==0:
            return 0
    return 1
number=600851475143
for i in range(2,int(math.sqrt(number))):
    if number%i==0:
        res=primechecker(i)
        if res==1:
            candidate+=[i]
print("Largest : ",max(candidate))

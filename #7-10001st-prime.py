import math
def primechecker(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1



count=0
for i in range(2,11111111111):
    if primechecker(i)==1:
        count+=1
    if count==10001:
        print("Number is : ",i)
        break


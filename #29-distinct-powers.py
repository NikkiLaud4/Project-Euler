arr=[]
dup=0
for a in range(2,101):
    for b in range(2,101):
        if(a**b not in arr):
            arr+=[a**b]
length=len(arr)
arr=sorted(arr)
print("Length: ",length,"\nArray: ",arr)

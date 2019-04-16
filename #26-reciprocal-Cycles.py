top=int(input("Upper Limit of denominator"))
edit=int(input("Will be resolving to 10 places Enter 1 to edit"))
if edit==1:
    upper=int(input("Resolve to how many places?"))
else:
    upper=10
maxx=1
for d in range(2,top):
    flag=0
    frac=[]
    a=10
    
    for i in range(0,upper):
        r=a%d
        frac+=[int(a/d)]
        for j in range(0,i):
            if (frac[-1]==frac[j] and frac[-2]==frac[j-1]):
                flag=i-j
        a=r*10
    print(frac)
    print('Yes!',d,' Iterates by',flag,'Places')
    if flag>maxx:
        maxx=flag
        winner=d
print('Biggest ever Iteration=',winner,'by',maxx,' places')
  


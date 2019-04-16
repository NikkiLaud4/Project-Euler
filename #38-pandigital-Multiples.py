#minimum n=2 (n>1), therefore number must be maximum 4 digits
maxx=[0]*9
winner=0
for num in range(10000):
    prod=[]
    check=[0]*10
    for mul in range(1,10):
        temp=num*mul
        if(temp%10==0):
            break
        temp=int(str(temp)[::-1])
        br=0
        while(temp>0):
            lsb=int(temp%10)
            if lsb==0:
                br=1
                break
            temp=int(temp/10)
            if(check[lsb]==0):
                prod+=[lsb]
                check[lsb]=1
            else:
                br=1
                break
        if br>0:
            break 
        if (len(prod)==9):
            print(num,prod)
            for count in range(0,9):
                if(prod[count]<maxx[count]):
                    break
                if(prod[count]>maxx[count]):
                    maxx=prod
                    winner=num
                if(prod[count]==maxx[count]):
                    continue
print("winner is:",winner,"with sequence:",maxx)
                
        
            

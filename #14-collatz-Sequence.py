Limit=int(input("Enter Limit: "))
maxx=1
winner=1
for i in range(1,Limit):
    n=i
    arr=[i]
    while(n!=1):
        if((n%2)==0):
            n=n/2
        else:
            n=3*n+1
        arr+=[n]
    length=(len(arr))
    print(i,"-->",arr,"Length=",length)
    if(length>maxx):
        maxx=length
        winner=i
print("winner is",winner)
    
    
        

num=2520
flag=0
while(flag==0):
    iflag=0
    for i in range(2,21):
        if num%i==0:
            iflag+=1
    if iflag==19:
        print("Smallest Number : ",num)
        flag=1
    num+=20

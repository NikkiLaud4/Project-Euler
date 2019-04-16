abundant=[]
arr=[0]
limit=int(input("Enter Limits:"))
for num in range (12,limit):
    div=[]
    for i in range(1,num):
        if(num%i)==0:
            div+=[i]
    if (num<sum(div)):
        abundant+=[num]
print("Abundants:\n",abundant)
for i in range(1,limit):
    flag=0
    for j in abundant:
        if i-j in abundant:
            flag=i
            break
    if (flag==0):
        arr+=[i]
print("Non Abundant-Sums\n",arr)

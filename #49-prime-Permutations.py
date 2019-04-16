
#The Prime Validator
def isprime(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=1
    if (count>1):
        return 0
    else:
        return 1

#The Permutation Validator
def seq(n):
    s=''
    b=n
    while(b>0):
        s+=str(b%10)
        b=int(b/10)
    return(sorted(s))
    



for num in range(1000,3401):
    if num%2==0:
        continue
    if (isprime(num)==1):
        num1=num+3330
        if (isprime(num1)==1):
            num2=num1+3330
            if(isprime(num2)==1):
               s=seq(num)
               ss=seq(num1)
               sss=seq(num2)
               if s==ss==sss:
                    print("Sequence be:",num,num1,num2)
                    print("================*********************================")
        

f=0
s=1
sm=0
while(s+f<4000000):
    s=s+f
    f=s-f
    if s%2==0:
        sm+=s
print("Sum : ",sm)
        

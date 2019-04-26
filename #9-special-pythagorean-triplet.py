
def pyth(a,b):
    c=1000-(a+b)
    if((c**2)==(a**2)+(b**2)):
        {
            print("Values:",a,b,c,"\nSum:",a+b+c,"\nProduct:",a*b*c)
            
        }
        
for i in range(1,1000):
    for j in range(999,1,-1):
        pyth(i,j);

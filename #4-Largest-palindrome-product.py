largest=0

def palchecker(a):
    if str(a)==str(a)[::-1]:
        return 1
    return 0


for i in range(100,1000):
    for j in range(100,1000):
        if palchecker(i*j)==1:
            if i*j > largest:
                largest=i*j
                print(i,j,i*j)
print("Largest Palindrome: ",largest)

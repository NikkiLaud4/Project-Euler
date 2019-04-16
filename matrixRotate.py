ch=1
while (ch==1):
 row=int(input('Enter Rows and cols'))
 if (row==0 or row==1):
    print('Nothing to show')
 arr=[]
 for i in range(row):
    arr+=[0]
 for i in range(row):
    arr[i]=[0]*row
 for i in range(row):
    for j in range(row):
        print('Enter',i+1,'ror,',j+1,'col Element:')
        arr[i][j]=int(input())
 for i in range(0,row):
    print(arr[i])
 if (row==0 or row==1):
    print('its OVER')
    continue
 k=int(input('Displacement:'))
 disp=[]
 min=[0]
 max=[row-1]
 for i in min:
    for j in range(row):
        disp+=[arr[i][j]]
 for i in max:
    for j in range(1,row):
        disp+=[arr[j][i]]
 for i in max:
    for j in range(row-2,-1,-1):
        disp+=[arr[i][j]]
 for i in min:
    for j in range(row-2,0,-1):
        disp+=[arr[j][i]]
 print(disp)
 l=len(disp)
 print('disp len=',l)

 for i in min:
    for j in range(row):
        arr[i][j]=disp[k]
        k+=1
 for i in max:
    for j in range(1,row):
        if (k>=l):
            k=k-l
        arr[j][i]=disp[k]
        k+=1        
 for i in max:
    for j in range(row-2,-1,-1):
        if (k>=l):
            k=k-l
        arr[i][j]=disp[k]
        k+=1
 for i in min:
    for j in range(row-2,0,-1):
        if (k>=l):
            k=k-l
        arr[j][i]=disp[k]
        k+=1
 for i in range(row):
  print(arr[i])
 ch=int(input('Enter 1 to go again!\n0 to Exit'))

    


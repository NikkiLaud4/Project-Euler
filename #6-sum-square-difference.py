sumsqr=0
sqrsum=0
for i in range(1,101):
    sumsqr+=i**2
    sqrsum+=i
sqrsum**=2
print("Difference : ",sqrsum-sumsqr)

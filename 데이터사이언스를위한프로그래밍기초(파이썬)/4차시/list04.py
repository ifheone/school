a=[]
for i in range(0,5):
    a.append(0)
add1=0
for i in range(0,5):
    a[i]=int(input(str(i+1)+"번째 숫자:"))
    add1=add1+a[i]
print("합계: %d" %add1)

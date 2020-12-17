k=[int(i) for i in input().split()]
a=0
b=0
for i in k:
    if i%2==0:
        a+=1
    elif i%2!=0:
        b+=1
if a>0 and b>0:
    print('YES')
else:
    print('NO')
    

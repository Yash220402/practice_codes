n=int(input())
s=0
p=1
for i in range(n):
    a=(int(input())) 
    while(a%10==0):
        s+=1
        a//=10
    p*=a
print(str(p)+"0"*s)
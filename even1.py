a1,a2=input().split()
a1=int(a1)
a2=int(a2)
for i in range(a1+1,a2+1):
    if(i % 2 == 0):
        print(i,end=" ")

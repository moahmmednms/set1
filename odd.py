a1,b2=input().split()
a1=int(a1)
b2=int(b2)
for i in range(a1+1,b2):
    if(i % 2 != 0):
        print(i,end=" ")

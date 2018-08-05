val1,val2=input().split()
val1=int(val1)
val2=int(val2)
for i in range(val1,val2+1):
    if(i % 2 != 0):
        print(i,end=" ")

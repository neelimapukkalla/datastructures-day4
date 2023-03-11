n=int(input("enter size"))
a=list(map(int,input().split(' ')))[n:]
s=0
for i in a:
    s=s+i
print(s)

c1=int(input())
v1=list(map(int,input().split()[:c1]))
v1.sort()
for i in v1:
   print(i,end=" ")

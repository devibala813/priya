c=int(input())
v=list(map(int,input().split()[:c]))
for p in range(c):
   print(v[p],p)

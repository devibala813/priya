d=int(input())
e=list(map(int,input().split()[:d]))
e.sort()
for i in e:
   print(i,end=" ")

d=int(input())
n1,n2=0,1
print(n2,end=" ")
for i in range(1,d):
 n3=n1+n2
 print(n3,end=" ")
 n1,n2=n2,n3

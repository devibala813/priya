n1,n2=list(map(int,input().split()))
count=0
for num in range(n1,n2+1):
 if(num>1):
  for i in range(2,num):
   if num%i==0:
    break
  else:
    count+=1
print(count)

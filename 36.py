d=input()
f=0
for i in range(len(d)):
 if(d[i].isdigit() or d[i].isalpha() or d[i]==(" ")):
  continue
 else:
  f+=1
print(f)

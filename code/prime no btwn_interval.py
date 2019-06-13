m,n=map(int,input().split())
for q in range(m+1,n):
  if q>0:
    for d in range (2,q):
      if(q%d==0):
        break
    else:
      print(q,end=' ')
  else:
    break

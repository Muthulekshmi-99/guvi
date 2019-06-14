a=int(input())
x=list(map(int,input().split()))
if (a==len(x)):
  x.sort()
  for i in x:
    print(i,end=' ')

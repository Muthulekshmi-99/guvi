a=int(input())
x=list(map(int,input().split()))
x.sort()
for i in range(0,a):
  print(x[i],end=' ')

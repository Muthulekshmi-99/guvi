n,l=map(int,input().split())
for i in range (n+1,l):
  a=i
  o=0
  while (a>0):
    m=a%10
    a=a//10
    c=m**3
    o=o+c
    if(i==o):
      print(i,end=' ')

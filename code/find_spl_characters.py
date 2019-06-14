st=input()
num=0
for i in range(len(st)):
  if(st[i].isdigit() or st[i].isalpha() or st[i]==' '):
    continue
  else:
    num=num+1
print(num)  

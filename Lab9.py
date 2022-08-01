import re
import math
file = open(r"laboratorio09.txt", 'r')
s =file.read()
bytes=[s[i:i + 8] for i in range(0, len(s), 8)]


def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

for i in range (len(bytes)):
       bytes[i]=int(bytes[i])

print(toString(bytes))


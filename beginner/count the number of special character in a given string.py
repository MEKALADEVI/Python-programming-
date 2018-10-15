import re
x=input("c=")
n=re.sub('[\w]','',x)
print(len(n))

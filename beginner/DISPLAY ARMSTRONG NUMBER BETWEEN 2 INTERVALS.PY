N=int(input("a="))
M=int(input("b="))
for x in range(N,M+1):
   order=len(str(x))
   sum=0
   t=x
   while t>0:
      y=t%10
      sum+=y**order
      t//=10
   if(x==sum):
      print(x)

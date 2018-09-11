N=int(input("a="))
M=int(input("b="))
flag=0
for x in range(N+1,M):
   flag=0
   for y in range(1,x+1):
        if(x%y==0):
           flag=flag+1
   if(flag==2):
         print(x)

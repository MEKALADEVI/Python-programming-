R=int(input("n=")) 
S=int(input("a=")) 
T=int(input("d=")) 
if(1<=R<=100000):
   sum=0
   i=0
   while i<R : 
      sum=sum+S
      S=S+T
      i=i+1
   print(sum) 
else:
    print("invlid")
 

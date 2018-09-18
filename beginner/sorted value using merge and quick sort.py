A=[]
N=int(input("n="))
if(1<=N<=1000):
  print("enter your",N,"integer")
  for i in range(1,N+1):
    a=int(input("c="))
    A.append(a)
  print(sorted(A))
else:
    print("invalid")

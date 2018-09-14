A=[]
N=int(input("n="))
if(1<=N<=100000):
  print("enter your",N,"integer")
  for i in range(1,N+1):
    a=int(input("c="))
    A.append(a)
  print(A)
  m=A[-1]
  for i in A:
     if m<i:
        m=i
  print("max",m)
else:
    print("invalid")

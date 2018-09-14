A=[]
N=int(input("n="))
if(1<=N<=1000):
  print("enter your",N,"integer")
  for i in range(1,N+1):
    a=int(input("c="))
    A.append(a)
  print(A)
  m=A[-1]
  for R in range(len(A)):
      for S in range(R,len(A)):
          if(A[R]>A[S]):
             A[R],A[S]=A[S],A[R]
  print("sorted list",A)
else:
    print("invalid")

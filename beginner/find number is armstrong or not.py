N=int(input("n="))
if(N<=100000):
 t=N
 rev=0
 while N>0:
    rem=N%10
    rev=rev+rem*rem*rem
    N=N//10
 if(rev==t):
    print("armstrong")
 else:
    print("not armstrong")
else:
    print("invalid")

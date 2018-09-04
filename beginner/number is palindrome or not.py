N=int(input("n="))
if(N<=1000):
 y=N
 rev=0
while N>0:
 rem=N%10
 rev=rev*10+rem
 N=N//10
if(y==rev):
  print("palindrome")
else:
  print("not palindrome")

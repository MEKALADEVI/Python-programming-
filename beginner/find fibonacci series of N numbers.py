N=int(input("enter number values:"))
a=0
b=1
print("fibonacci series is:")
print(b)
for i in range(1,N):
    next=a+b
    print(next)
    a=b
    b=next

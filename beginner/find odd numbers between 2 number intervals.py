s=int(input("N="))
e=int(input("C="))
if(N<=100000):
   for x in range(s+1,e):
         if(x%2!=0):
            print(x)
else:
    print("invlid")        

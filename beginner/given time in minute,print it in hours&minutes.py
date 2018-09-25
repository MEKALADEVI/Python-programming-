r=int(input("m="))
i=0
s=0
for u in range(1,25):
    for v in range(1,61):
        s=s+1
        if(r==s):
            print(i,":",v)
            break;
    i=i+1

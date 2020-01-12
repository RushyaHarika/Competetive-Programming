count=0
temp=0
pro=1
while(count<3):
    num=int(input("Enter a number"))
    count=count+1
    if (num==7):
        pro=1
        if (num==7 and count==3):
            temp=-1
    else:
        pro=num*pro
if (temp==-1):
    pro=-1
print(pro)
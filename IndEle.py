l=[]
nind=0
while(True):
    ind=int(input("Enter index"))
    num=int(input("Enter number at index"))
    if ind>=20:
        break
    else:
        for i in range(nind,ind):
            if len(l)<=ind:
                l[ind]=num
            else:
                l.append(0)
        l.append(num)
        nind=ind+1
        print(l)
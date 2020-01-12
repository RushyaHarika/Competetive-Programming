def fun(l):
    l1=[]
    for i in range(len(l)):
        if l[i]%10!=6:
            l1.append(l[i])
        elif l[i]%10==6:
            if i!=0 and i!=len(l)-1:
                if l[i-1]%10!=6 and l[i+1]%10!=6:
                    l1.append(l[i])
            elif i==0:
                if l[i+1]%10!=6:
                    l1.append(l[i])
            elif i==len(l)-1:
                if l[i-1]%10!=6:
                    l1.append(l[i])
    print(l1)
    return l1
    
if __name__=="__main__":
    l=[]
    while True:
        n=int(input())
        if n==-1:
            break
        else:
            l.append(n)
    p=fun(l)
    for i in p:
        print(i)
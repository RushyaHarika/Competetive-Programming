def fun(l):
    r=[]
    l1=[]
    l2=[]
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            if l2!=[]:
                m=len(l2)
                r.append(m)
                l2=[]
            l1.append(l[i])
        else:
            if l1!=[]:
                m=len(l1)
                r.append(m) 
                l1=[]
            l2.append(l[i])
    return max(r)
if __name__=="__main__":
    l=[]
    while True:
        n=int(input())
        if n==-1:
            break
        else:
            l.append(n)
    p=fun(l)
    print(p)
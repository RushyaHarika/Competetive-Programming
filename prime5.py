s1="zyxwvutsrqponmlkjihgfedcba"
s2="abcd"
l=sorted(s2,key=lambda x:s1.index(x))
s="".join(l)
print(s)
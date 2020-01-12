s=input()
r=(s+s).find(s,1,-1)
out=-1 if r==-1 else s[:r]
print(out)
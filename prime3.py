vo=list("aeiouAEIOU")
s=input()
n=len(s)
t=n*(n+1)//2
v=0
for i in range(n):
    if s[i] in vo:
        v+=len(s)-i
print("vowels=",v)
print("Consonants=",t-v)

s=input()
d=['{}','[]','()']
while any(x in s for x in d):
    for i in d:
        s=s.replace(i,"")
if len(s)==0:
    print(True)
else:
    print(False)
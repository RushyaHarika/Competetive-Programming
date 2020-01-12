sal=float(input("Enter Salary"))
jl=int(input("Enter job level"))
if jl==3:
    hike=15
elif jl==4:
    hike=7
elif jl==5:
    hike=5
else:
    hike=0
if hike==0:
    finalsal=sal
else:
    finalsal=(sal*hike/100)+sal
print(finalsal)
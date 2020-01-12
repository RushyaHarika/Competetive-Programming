typ=input("Enter V or N")
dist=int(input("Enter distance"))
quantity=int(input("Enter Quantity"))
if typ=="V":
    cost=120
if typ=="N":
    cost=150
if dist<=3:
    dcost=0
elif dist>3 and dist<=6:
    dcost=(dist-3)*3
else:
    dcost=(dist-6)*6+9
total=dcost+(cost*quantity)
print(total)
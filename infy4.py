five=int(input("Enter five coins"))
one=int(input("Enter one coins"))
amount=int(input("Enter amount to be paid"))
if (amount//5)<=five and (amount%5)<=one:
    print("Five=",(amount//5))
    print("One=",(amount%5))
elif (amount//5)>five and one>=(amount-(five*5)):
    print("Five=",five)
    print("One=",amount-(five*5))
else:
    result=-1
    print(result)
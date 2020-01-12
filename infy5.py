rupees=int(input("Enter the rupees required "))
currency=input("Enter the currency that the traveller has ")
if currency=="euro":
    amount=rupees*0.01417
    print("{} euros".format(amount))
elif currency=="british pound":
    amount=rupees*0.0100
    print("{} british pounds".format(amount))
elif currency=="australian dollar":
    amount=rupees*0.02140
    print("{} australian dollars".format(amount))
elif currency=="canadian dollar":
    amount=rupees*0.02027
    print("{} canadian dollars".format(amount))
else:
    print(-1)
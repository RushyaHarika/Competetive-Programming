mileage=int(input("Enter Mileage"))
charge=int(input("Enter the amount per litre"))
dist=int(input("Enter Distance"))
final=((dist*2)*charge)/(mileage*4)
print(final)
if final%5==0:
    print("True")
else:
    print("False")
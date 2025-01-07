bill=int(input("Enter the bill"))
tip=int(input("Enter the tip"))
if tip==0:
    print(f"total amount:{bill}")
else:
    totalBill=bill+(bill*tip/100)
    print("totalBill"+str(totalBill))
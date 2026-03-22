print("Welcome to the tip calculator")
total_bill=int(input("What was the total bill? "))
Tip=int(input("How much tip would you like to give?10,12 or 15"))
split=int(input("how many people to split the bill with:"))
num=((total_bill*Tip/100)+total_bill)/split
print("You need to give:"+str(num))

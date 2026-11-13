# Tip calculator 
# welcome to the tip calculator!
# What was  the total bill? $150
# How much tip would you like  to give ?10 , 12 or 15 ? 12
# How many people do split the bill? 5
# Each person should pay: $33.60

print("Welcome to yhe tip calculator!")
bill =   float(input("What was the total  bill? $"))
tip =    int(input("How much tip would you like to give? 10 , 12  or  15?"))
person_split = int(input("How much person do split the bill?"))
tip_percent = (tip / 100)
bill_with_tip = (bill * tip_percent)
total_bill = (bill + bill_with_tip)
total_bill_per_split =  (total_bill / person_split )

Final_result = round(total_bill_per_split , 2)
print(f"Each person should  pay:{Final_result}" )

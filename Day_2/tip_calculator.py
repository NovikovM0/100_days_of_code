print("Hello user! Welcome to tip calc.")
total_bill = float(input("What was the total bill in $"))
tip_percentage = int(input("How much tip you would like to give in percentage? 10%, 15% or your number?"))
users_amount = int(input("How many people to split the bill?"))
bill_per_person = (total_bill + total_bill * (tip_percentage / 100)) / users_amount
final_bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_bill_per_person}")
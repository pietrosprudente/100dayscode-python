print("Welcome to the tip counter")
bill = float(input("What was the total bill $"))
tip = int(input("How much tip would you like to give?(Do not add %) 10, 12, or 15"))
people = int(input("How many Humans do you want to split the bill"))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final = round(bill_per_person, 2)
print(f'Each person should pay: ${final}')

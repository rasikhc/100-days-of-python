print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_per_person = (bill / people) * (tip/100)
bill_per_person = (bill/people) + tip_per_person
final_bill_per_person = round(bill_per_person,2)
print(final_bill_per_person)
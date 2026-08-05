print("Welcome to Python Pizza Deliveries!")

S = 15
M = 20
L = 25
Bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    Bill = S
elif size == "M":
    Bill = M
else:
    Bill = L
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if Bill == 15:
        Bill += 2
    elif Bill > 15:
        Bill += 3
else:
    Bill += 0

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    Bill += 1
else:
    Bill += 0

print(f"Your final bill is: ${Bill}.")

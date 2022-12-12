#greet user
print("Welcome to Louis' pizza parlour!")

#ask user to enter pizza size
diameter = float(input("Enter the diameter  (inches):"))

#declare constants
RENTAL_COST= 1
MATERIALS = 0.5
LABOUR COST = 0.75
HST = 0.13

#calculate the subtotal
subtotal = RENTAL_COST + LABOUR_COST + MATERIALS * diameter

#calculate the tax
tax = subtotal * HST

#calculate total
total = tax + subtotal

#display the subtotal tax and total to the user

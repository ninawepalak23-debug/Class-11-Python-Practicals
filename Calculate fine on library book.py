cost = float(input("Enter cost of book: "))
days = int(input("Enter number of days: "))

rent = cost * (1 / 100) * days

if days <= 5:
    fine = 0

elif days <= 10:
    fine = (days - 5) * 3.5

else:
    fine = (5 * 3.5) + (days - 10) * 5.5

total = rent + fine

print("Rent =", rent)
print("Fine =", fine)
print("Total =", total)

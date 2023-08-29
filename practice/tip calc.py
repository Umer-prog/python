print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10,12,15 "))
people = int(input("How many people to split the bill? "))
extra = (tip_percent / 100) + 1
final = total * extra
per_person  = "{:.2f}".format(final / people)
print(f"Each person should pay: {per_person}")
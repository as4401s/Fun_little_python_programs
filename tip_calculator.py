print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

calc = float(bill)+((float(tip)*float(bill))/100)
calc_final = calc/float(people)
cal_final_rounded = round(calc_final,2)

print(f"Each person should pay: ${cal_final_rounded}")
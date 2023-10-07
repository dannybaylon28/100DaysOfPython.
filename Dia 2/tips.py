print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

people = int(input("How many people to split the bill? "))

tip = int(input("What porcentage tip would you like to give? 10, 12 or 15? "))

if tip == 10:
    total_bill = float(bill*0.10)+bill
    total = round(total_bill/people, 2);
    print(f"Each person should pay: ${total}")

elif tip == 12:
    total_bill = float(bill*0.12)+bill
    total = round(total_bill/people, 2);
    print(f"Each person should pay: ${total}")

elif tip == 15:
    total_bill = float(bill*0.15)+bill
    total = round(total_bill/people, 2);
    print(f"Each person should pay: ${total}")  

else:
    print("Please, type a valid number")    



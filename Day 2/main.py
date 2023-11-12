#Prompt User with Welcomeing statement:
# Welcome to the tip calculator
# Ask "What was the total bill? {userInput}"
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill? {userInput}
# Each person should pay: $amount

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage_of_tip = int(input("What percent tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))
total_per_person = round((total_bill + (percentage_of_tip / 100 * total_bill)) / people_to_split, 2)
print(f"Each person should pay: {total_per_person}")
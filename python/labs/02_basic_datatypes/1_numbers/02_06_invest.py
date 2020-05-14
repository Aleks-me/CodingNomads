'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = float(input("Please, enter investment amount: "))
rate = float(input("Please, enter investment rate in % (e.g. 0.15): "))
years = int(input("Please, enter how many years to invest: "))

future_value = amount * (1 + rate / 12) ** (12 * years)

if years < 0:
    print("You can't travel to the past, sorry.")
else:
    print(f"Your total money for {years} years:", future_value)

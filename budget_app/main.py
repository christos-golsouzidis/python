# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart

'''
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)


print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
#'''

#'''
occasional = budget.Category('Occasional')
accidental = budget.Category('Accidental')
tech = budget.Category('tech')
entertainment = budget.Category('entertainment')

occasional.deposit(400, 'initial deposit!! YEAH!!!')
occasional.withdraw(8.22)
occasional.withdraw(15, 'döner')
entertainment.deposit(200)
occasional.withdraw(40.75, 'supermarkt')
occasional.deposit(100 , '2. deposit')
occasional.transfer(50, accidental)
entertainment.withdraw(21, 'Cinema')
entertainment.withdraw(18, '>BG')
occasional.withdraw(6.8, 'Tickets')
occasional.transfer(100, tech)
tech.withdraw(19.99, 'usb stick')
tech.withdraw(4.99, 'WLAN adapter')
accidental.withdraw(30)
tech.deposit(5)
print(occasional)
print(accidental)
print(tech)

print(create_spend_chart([occasional, accidental, entertainment, tech]))
#'''
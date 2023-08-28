cost_of_one_UC = 20 / 60
cost_of_60_UC = 20

quantity = int(input("How much UC do you want to buy? "))

total_cost = quantity * cost_of_one_UC

amount = str(total_cost)
currency = "ZAR"
formatted_amount = "{0} {1}".format(currency, amount)

print("That'll cost you", formatted_amount)

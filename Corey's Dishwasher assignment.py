#The Declarations
item_name = "Dishwasher"
retail_price = 325.0
wholesale_price = 200.0

#The Calculations
retail_profit = retail_price - wholesale_price
sale_price = retail_price - (retail_price * 0.25)
sale_profit = sale_price - wholesale_price

#The Ouputs
print("The name of the item is:", item_name)
print("The current retail price is: $" + str(retail_price))
print("The current wholesale price: $" + str(wholesale_price))
print("The retail profit is: $" + str(retail_profit))
print("The sale price should be: $" + str(sale_price))
print("The sale profit will be: $" + str(sale_profit))

# Get the buy price and sell price from the user
buy_price = float(input("Enter the price you can win bids for: "))
sell_price = float(input("Enter the price you can sell for within the hour: "))
number_to_keep = float(input("Enter how many cards do you need to keep for the SBC: "))

# Calculate the profit per gold common
profit_per_common = sell_price - buy_price

total_keep_price = number_to_keep * buy_price 
total_sell_price = 0

while total_sell_price < total_keep_price:
    total_sell_price += profit_per_common

number_to_sell = total_sell_price / profit_per_common

# Print the result
print("\n")
print("Profit per common: ", int(profit_per_common))
print("\n")
print("Total sell price: ", int(total_sell_price))
print("\n")
print("You need to buy", int(number_to_sell + 8), "gold commons to brake even if you keep 8 of them.")
print("\n")
print("You need to sell", int(number_to_sell), "gold commons to brake even.")
print("\n")

stock = input ("Which Stock you are scanning ? ")
print("it is", stock)
Stock_Price = float(input ("What is current price of " + stock +" ? "))
print ("current price of " + stock + "is", Stock_Price)
Qty = 1000
price_upper_range = 1300
price_lower_range = 1250
if Stock_Price >= price_upper_range:
    print ("Price of", stock, "is above", price_upper_range, "Buy", Qty)
elif Stock_Price <= price_lower_range:
    print ("Price of", stock,"is below", price_lower_range, "Sell", Qty)
else:
    print ("price of", stock, "is range bound between",price_lower_range,"and",price_upper_range, "hence Hold the current position")
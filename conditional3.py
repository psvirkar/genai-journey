stock = "Reliance"
price = 1275
Qty = 100
if stock :
    if price > 1300:
        print ("price of", stock, "is above", price, "Buy", Qty)
    elif price < 1250:
        print ("price of", stock, "is below", price, "Sell", Qty)
    else:
        print ("Since price of", stock, "is range bound between 1250 and 1300 Hold the current position")
stock = "Reliance"
price = 1240
price1 = 1300
price2 = 1250
Qty = 100
if stock:
    if price >= price1:
        print ("Price of", stock, "is above", price1, "Buy", Qty)
    if price <= price2:
        print ("Price of", stock, "is below", price2,"Sell",Qty)
    if price2 < price < price1:
        print("Price of", stock,"is in between", price2, "and", price1, "hence, Hold the position")
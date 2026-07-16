stock = "Reliance"
price = 1275
price1 = 1301
price2 = 1249
Qty = 100
if stock:
    if price1 >= 1300:
        print ("Price of", stock, "is above", price1, "Buy", Qty)
    if price2 <= 1250:
        print ("Price of", stock, "is below", price2,"Sell",Qty)
    if price >= price2 and price <= price1 :
        print("Price of", stock,"is in between", price2, "and", price1, "hence, Hold the position")
    
# conditional final assigment using and, or, not, ternary, truthiness functions
# creating market open with actual time stamp
import datetime
weekday = datetime.datetime.now().weekday() < 5
current_time = datetime.datetime.now().time()
market_start = datetime.time (9, 15)
market_close = datetime.time (15, 30)
market_open = weekday and (market_start <= current_time <= market_close) # referring actual day and time from PC
# pricing, volume and positions details
current_price = 1249.5732
pre_cl_price = 1294.2991
# ternary operator chnage in price status 
change = current_price - pre_cl_price, ("Gain" if current_price - pre_cl_price > 0 else ("Loss" if current_price -pre_cl_price < 0 else "No change"))
current_volume = 480000
avg_volume = 475583
upper_range_price = 1300
lower_range_price = 1250
price_alert = current_price >= upper_range_price or current_price <= lower_range_price
buy_signal = current_price >= upper_range_price
sell_signal = current_price <= lower_range_price
hold_pstn = not buy_signal and not sell_signal, "Hold current status"
max_pstn_trhold = 5000
current_hld_pstn = 4000
bal_room_hld_pstn = max_pstn_trhold - current_hld_pstn
Buy_order = ("Bought",bal_room_hld_pstn)
Sell_order = ("Sold",current_hld_pstn)
# truthiness conditions
open_alert = []
# if conditions nested
if market_open :
    print("Market is Open")
    if current_volume >= avg_volume and bal_room_hld_pstn >= 0:
        print("Volume and balance holding position conditions met. Waiting for price aleert for executing order")
# truthiness condition added
        if open_alert :
            print(f"System open alert generated: {open_alert}")
        else:
            print("No open alert generated")
        if price_alert:
            print("ALERT! ALERT!! ALERT!!!. Price moved beyond Range", "upward" if buy_signal else "downward")
            action_executed = Buy_order if buy_signal else (Sell_order if sell_signal else hold_pstn)
            print("As per signal generated action executed", action_executed)
    else: print ("Either Volume or balance room for holding position not met wait until condition met")
else: print ("Market is not open yet wait till market opens")

# printing complete market status report
if market_open:
    Market_Status = f"""
Current Market Status Report ===

********************************
Is market open? : {market_open}
What is current price?: {current_price}
what was previous closing price?: {pre_cl_price}
What is change from previous price?: {change}
What is current volume?: {current_volume}
What is average volume?: {avg_volume}
Is volume condition met?: {"Yes" if current_volume > avg_volume else "No"}
Is price beyond range and generated alert?: {price_alert}
Is this buy or sell signal?: {"Buy" if buy_signal else ("Sell" if sell_signal else hold_pstn )}
What is balance room for buying from holding position: {"None" if sell_signal else bal_room_hld_pstn}
What is order quantity?: {Buy_order if buy_signal else Sell_order if sell_signal else None}
"""
    print(Market_Status)
else: 
    print("Market is not open hence, no Market Status Report")
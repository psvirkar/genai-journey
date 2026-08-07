# in first variable exercise lot of functions were missing being coverred in this final assignment
raw_data = ("      reliance industries ,     1275.73845731 ,      1300.21364727 ")
# spliting string raw_data with comma separator
part_raw_data = raw_data.split(",")
# removing extra spaces from list of part_raw_data
stock_name = part_raw_data[0].strip()
current_price = float(part_raw_data[1].strip())
previous_closing_price = float(part_raw_data[2].strip())
# creating new clean_stock_data
#clean_stock_data = [stock_name, current_price, previous_closing_price]
#print(clean_stock_data)
# printing stock_name first letter of each word in upper case
#print(stock_name.title())
# printing stock_name all letters in upper case in ticker style 
#print(stock_name.upper())
# printing stock_name all letters in lower case in search style
#print(stock_name.lower())
# printing current_price and previous_closing_price
#print("Current Price: Rs.", current_price, "Previous Closing price: Rs.", previous_closing_price)
# calculating change from previous_closing_price and current_price
change = (current_price - previous_closing_price)
#print("Change from previous closing price : Rs.", change)
# printing absolute value of change
#print("Absolute change from previous closing price :Rs.", abs(change))
# using rounding function upto 4th decimals as market practice (rounding is not market practice)
#print("Change from previous closing price rounded to 4th decimals : Rs.", round(change,4))
# calculatimg change in %
change_in_pctage = round((change/previous_closing_price)*100,4)
#print("Change in price in percentage pto 4th decimal :", change_in_pctage,"%")
# creating boolean for gain in price true else same or loss false
gain = change>0
#print("Has price gained from previous closing price? :", gain)
# creating another boolean to check text exist in vaiable note in function is case sensative
industries = "industries" in raw_data
#print("Does word industries exist in raw_data? :", industries)
# projecting price 3 days later. Considering change in %, in previous closing price continues at same rate. Here 3 day is exponent
projected_price = current_price*(1+(change_in_pctage/100))**5
#print("If price moves in same direction at same rate, what would be the price after 5 days? :", round(projected_price,4))
# joining strings and integer / flaot you need to convert integer / float to string and then join so create separate variable
round_curnt_pr = round(current_price,4)
#print("What is current price of stock? :")
#print("-".join([stock_name.title(),str(round_curnt_pr)]))
# applying truncating function current price, preevious closing price and change
import math
def truncate(price,decimals):
    factor = 10**decimals
    return math.trunc(price*factor) / factor
prices = [current_price,previous_closing_price,change]
truncated_prices = []
for p in prices:
    truncated_prices.append(truncate(p,4))
print(truncated_prices)
# creating final report using fstring
final_output = f"""
Stock: {stock_name.title()}
Ticker tag: {stock_name.upper()}
Search tag: {stock_name.lower()}
Current price: {round_curnt_pr}
Change: {round(change,4)} 
Did previous closing price gain?: {gain}
Absolute change: {round(abs(change),4)}
Percentage changed: {change_in_pctage} %
5th day projection if trend continues at same rate of gain: {round(projected_price,4)}
Does contain industries?: {industries}
Record Id: {'-'.join([stock_name.title(),str(round_curnt_pr)])}
"""
print (final_output)
def calculate_discount(price, discount_percent):
    if discount_percent >=20:
       discount_price = price*(1-discount_percent/100)
       return discount_price
       
    else:
        return price

price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the discount of the item:"))

final_price = calculate_discount(price, discount_percent)
                         
if final_price != price:
    print("Price after discount is:",final_price)
else:
    print("Oops! No discount, the price is:", price)
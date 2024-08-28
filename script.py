def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

#prompt the user to enter the original price
price = float(input("Please enter the original price:\n"))

#prompt the user to enter the discount percentage
discount_percent = float(input("Please enter the discount percentage:\n"))

#calculate the final price
final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print(f"The final price after applying the discount is: Sh{final_price:.2f}")
else: 
    print(f"No discount applied. The original price is: Sh{price:.2f}")
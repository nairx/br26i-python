def calculate_bill(price,quantity):
    total = price * quantity
    discount = total * 0.10
    final_amount = total - discount 
    return final_amount

amount = calculate_bill(1000,5)

print(amount)
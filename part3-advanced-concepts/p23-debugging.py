import logging

logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_bill(price,quantity):
    logging.info("Calculating Bill")
    logging.debug("price=%s",price)
    logging.error("quantity=%s",quantity)
    total = price * quantity
    logging.debug("total=%s",total)
    discount = total * 0.10
    final_amount = total - discount 
    return final_amount

amount = calculate_bill(1000,5)

print(amount)





# import logging

# logging.basicConfig(level=logging.ERROR)

# def calculate_bill(price,quantity):
#     logging.info("Calculating Bill")
#     logging.debug("price=%s",price)
#     logging.error("quantity=%s",quantity)
#     total = price * quantity
#     logging.debug("total=%s",total)
#     discount = total * 0.10
#     final_amount = total - discount 
#     return final_amount

# amount = calculate_bill(1000,5)

# print(amount)
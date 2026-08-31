products={
  1: {"name": "Laptop", "price": 50000},
  2: {"name": "Mouse", "price": 1000},
  3: {"name": "Keyboard", "price": 2000},
  4: {"name": "Headphones", "price": 3000},
  5: {"name": "Monitor", "price": 15000}
}
cart={}
def display_products():
    pass
def add_to_cart():
    pass
def view_cart():
    pass
def remove_from_cart():
    pass
def update_quantity():
    pass
def calculate_total():
    pass
def checkout():
    pass
def main():
    while True:
        print("\n")
        print("================================")
        print("    SHOPPING CART")
        print("================================")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Remove Product")
        print("5. Update Quantity")
        print("6. Calculate Total")
        print("7. Checkout")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice=="8":
            break

main()
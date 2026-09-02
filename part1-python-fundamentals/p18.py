# ==========================================
# SHOPPING CART CONSOLE APPLICATION
# ==========================================

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mouse", "price": 1000},
    3: {"name": "Keyboard", "price": 2000},
    4: {"name": "Headphones", "price": 3000},
    5: {"name": "Monitor", "price": 15000}
}

cart = {}


# ------------------------------------------
# Display Products
# ------------------------------------------

def display_products():

    print("\n========== PRODUCTS ==========")

    print(f"{'ID':<5}{'Product':<20}{'Price':>10}")
    print("-" * 35)

    for product_id, product in products.items():

        print(
            f"{product_id:<5}"
            f"{product['name']:<20}"
            f"₹{product['price']:>9}"
        )


# ------------------------------------------
# Add Product
# ------------------------------------------

def add_to_cart():

    display_products()

    try:
        product_id = int(input("\nEnter Product ID: "))

        if product_id not in products:
            print("Invalid Product ID")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        print(
            f"{quantity} x "
            f"{products[product_id]['name']} "
            f"added to cart."
        )

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# View Cart
# ------------------------------------------

def view_cart():

    print("\n========== SHOPPING CART ==========")

    if not cart:
        print("Cart is empty.")
        return

    total = 0

    print(f"{'Product':<20}{'Qty':<10}{'Price':<12}{'Subtotal'}")
    print("-" * 55)

    for product_id, quantity in cart.items():

        product = products[product_id]

        subtotal = product["price"] * quantity

        total += subtotal

        print(
            f"{product['name']:<20}"
            f"{quantity:<10}"
            f"₹{product['price']:<11}"
            f"₹{subtotal}"
        )

    print("-" * 55)
    print(f"Total: ₹{total}")


# ------------------------------------------
# Remove Product
# ------------------------------------------

def remove_from_cart():

    if not cart:
        print("\nCart is empty.")
        return

    view_cart()

    try:

        product_id = int(input("\nEnter Product ID to remove: "))

        if product_id in cart:

            removed_product = products[product_id]["name"]

            del cart[product_id]

            print(f"{removed_product} removed from cart.")

        else:

            print("Product is not in cart.")

    except ValueError:

        print("Please enter a valid Product ID.")


# ------------------------------------------
# Update Quantity
# ------------------------------------------

def update_quantity():

    if not cart:
        print("\nCart is empty.")
        return

    view_cart()

    try:

        product_id = int(input("\nEnter Product ID: "))

        if product_id not in cart:

            print("Product is not in cart.")
            return

        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:

            del cart[product_id]

            print("Product removed from cart.")

        else:

            cart[product_id] = quantity

            print("Quantity updated.")

    except ValueError:

        print("Please enter a valid number.")


# ------------------------------------------
# Calculate Total
# ------------------------------------------

def calculate_total():

    total = 0

    for product_id, quantity in cart.items():

        price = products[product_id]["price"]

        total += price * quantity

    return total


# ------------------------------------------
# Checkout
# ------------------------------------------

def checkout():

    if not cart:

        print("\nCart is empty.")
        return

    view_cart()

    total = calculate_total()

    print("\n========== CHECKOUT ==========")

    print(f"Total Amount: ₹{total}")

    confirm = input("Confirm order? (yes/no): ")

    if confirm.lower() == "yes":

        print("\nOrder placed successfully!")

        cart.clear()

    else:

        print("\nOrder cancelled.")


# ------------------------------------------
# Main Menu
# ------------------------------------------

def main():

    while True:

        print("\n")
        print("================================")
        print("       SHOPPING CART")
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

        if choice == "1":

            display_products()

        elif choice == "2":

            add_to_cart()

        elif choice == "3":

            view_cart()

        elif choice == "4":

            remove_from_cart()

        elif choice == "5":

            update_quantity()

        elif choice == "6":

            total = calculate_total()

            print(f"\nCart Total: ₹{total}")

        elif choice == "7":

            checkout()

        elif choice == "8":

            print("\nThank you for shopping!")

            break

        else:

            print("Invalid choice.")


# Start application

main()
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_items(self,item):
        self.items.append(item)
    def __len__(self):
        return len(self.items)

cart = ShoppingCart()

cart.add_items("Laptop")
cart.add_items("Mounse")
cart.add_items("Keyboard")

print(len(cart))

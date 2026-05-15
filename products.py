

class Product:
    def __init__(self, name: str, price: float, quantity: int ):
        if not name:
            raise ValueError("Names is need it required")
        if price <= 0:
            raise ValueError("Price must be above 0")
        if quantity < 0:
            raise ValueError("Quantity must be a positive number")
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
        except TypeError:
            print("Type the right data type")
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        if quantity == 0:
            self.deactivate()
        self.quantity = self.quantity + quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float: # quantity parameter represents the buying items from the client
        if quantity > self.quantity:
            raise ValueError("We cant cover this buying quantity.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.quantity * self.price



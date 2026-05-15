from products import Product

class Store:
    def __init__(self, product_list: list):
        self.product_list = product_list

    def add_product(self, product: Product):
        self.product_list.append(product)

    def remove_product(self, product: Product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> list[Product]:
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list) -> float:
        total_order = 0
        for item, quantity in shopping_list:
            total_order += item.buy(quantity)
        return total_order












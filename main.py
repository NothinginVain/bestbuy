from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def list_products(store_obj):
    products_list = store_obj.get_all_products()
    print('----------------------------')
    for index, product in enumerate(products_list, start=1):
        print(f'{index}. ', end='')
        product.show()
    print('----------------------------')


def show_total(store_obj):
    total = store_obj.get_total_quantity()
    print(f'\nTotal of {total} items in store')


def make_order(store_obj):
    products_list = store_obj.get_all_products()

    list_products(store_obj)

    shopping_list = []

    while True:
        print('When you want to finish order, enter empty text.')
        product_pick = input('Which product # do you want? ')
        if not product_pick:
            break
        selected_product = products_list[int(product_pick)-1]
        quantity_buy = int(input('What amount do you want? '))
        shopping_list.append((selected_product, quantity_buy))
        print('Product added to list!\n')

    total_price = store_obj.order(shopping_list)
    print('**********')
    print(f'Order made! Total payment: €{total_price}')


def star(store_obj):
    menu = {
        '1': list_products,
        '2': show_total,
        '3': make_order
    }
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == '4':
            print('Goodbye!')
            break

        menu.get(choice, lambda _: print('Invalid input'))(store_obj)


def main():
    star(best_buy)

if __name__ == "__main__":
    main()
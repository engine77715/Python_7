class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            result += f"{item}: {cnt} pcs.\n"
        return result.strip()

# Створення товарів
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

# Створення користувача
buyer = User("Ekaterina", "Shumeiko", "0549765504")

# Створення замовлення
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(lemon)  # lemon, price: 5
print(buyer)  # Ekaterina
print(cart)
"""
User: Ekaterina Shumeiko
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ekaterina Shumeiko
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
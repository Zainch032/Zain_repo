class Product:
    def _init_(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        return self.price * quantity

    def make_purchase(self, quantity):
        try:
            if quantity > self.amount:
                raise ValueError(f'Not enough product available. Quantity must be less than or equal to {self.amount}.')
            elif quantity <= 0:
                raise ValueError('Quantity must be greater than 0.')

            self.amount -= quantity
            total_price = self.get_price(quantity)
            
            print(f'You have successfully purchased {quantity} {self.name}(s).')
            print(f'Total price charged: ${total_price:.2f}')

        except ValueError as e:
            print(f'Error: {e}')

nose_pin = Product('Diamond Nose Pin', 50, 31000)
nose_pin.make_purchase(2)
print(f'Remaining Stock: {nose_pin.amount}')

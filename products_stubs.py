# Muhammad Zain (Sp23-Bai-032)
# Zaimal Zia (Sp23-Bai-043)

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity > self.amount:
            raise ValueError(f'Only {self.amount} units are available.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0.')

        total_price = self.price * quantity
        return total_price

    def make_purchase(self, quantity):
        try:
            total_price = self.get_price(quantity)

            # Update stock after the purchase
            self.amount -= quantity

            print(f'Successfully purchased {quantity} {self.name}(s).')
            print(f'Total price charged: ${total_price:.2f}')

            # Process payment
            payment = float(input('Enter payment amount: $'))
            if payment < total_price:
                raise ValueError('Insufficient payment. Please enter the correct amount.')
            else:
                change = payment - total_price
                print(f'Payment successful! Your change is: ${change:.2f}')
                print(f'Remaining stock: {self.amount}')

        except ValueError as e:
            print(f'Error: {e}')

# Example usage:
product = Product('Diamond Necklace', 50, 1500)

# Test the purchase
product.make_purchase(3)
print(f'After purchase, remaining stock: {product.amount}')


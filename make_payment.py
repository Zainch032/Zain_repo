class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.total_price = 0  # Initialize total price

    def get_price(self):
        try:
            quantity = int(input(f"How many {self.name}(s) do you want to purchase? "))

            if quantity <= 0:
                raise ValueError("You must purchase at least one item.")

            if quantity < 10:
                discount = 0
            elif 10 <= quantity < 100:
                discount = 10
            else:
                discount = 20

            self.total_price = quantity * self.price * (1 - discount / 100)
            print(f"You purchased {quantity} {self.name}(s) with a {discount}% discount.")
            print(f"Total price: ${self.total_price:.2f}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def make_payment(self):
        try:
            payment = float(input(f"Total amount due is ${self.total_price:.2f}. Enter payment amount: $"))

            if payment < self.total_price:
                raise ValueError("Insufficient payment. Please enter the correct amount.")
            elif payment > self.total_price:
                change = payment - self.total_price
                print(f"Payment successful! Your change is ${change:.2f}.")
            else:
                print("Payment successful! No change is due.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

product = Product("Widget", 100, 10)
product.get_price()

if product.total_price > 0:
    product.make_payment()

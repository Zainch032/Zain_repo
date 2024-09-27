def make_purchase(self, quantity):
        """Reduces the stock by the purchased amount and prints the total cost."""
        try:
            if quantity <= 0:
                raise ValueError("Purchase quantity must be greater than zero.")
            if quantity > self.amount:
                raise ValueError("Insufficient stock available.")

            total_price = self.get_price(quantity)
            self.amount -= quantity
            print(f"Purchased {quantity} items of {self.name} for ${total_price:.2f}.")
            print(f"Remaining stock: {self.amount}")

        except ValueError as e:
            print(f"Error: {e}")
class Product:
    def __init__(self, name, amount, price):
        """
        Initializes the Product object with a name, amount in stock, and price per unit.
        """
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
   
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if quantity < 10:
            discount = 0
        elif 10 <= quantity < 100:
            discount = 10
        else:
            discount = 20

        total_price = quantity * self.price * (1 - discount / 100)
        return total_price
    except Exception as e:
        print("An unexpected error occurred:", e)
    
     def make_purchase(self, quantity):
      pass


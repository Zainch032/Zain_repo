class Product:
  def _init_(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):   
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if quantity < 10:
            total_price = quantity * self.price
        elif 10 <= quantity < 100:
            total_price = quantity * self.price * 0.9  # 10% discount
        else:
            total_price = quantity * self.price * 0.8  # 20% discount
        
        return total_price


  def make_purchase(self, quantity):
      try:
        if quantity > self.amount:
            raise ValueError(f'Not enough product available. Quantity must be less than {self.amount}')
        elif quantity < 0:
            raise ValueError('Quantity must be greater than 0.')
        self.amount = self.amount - quantity
        price = self.get_price(quantity)
        print(f'Here\'s the total price charged: {price}')
      except ValueError as e:
         print(f'Error:{e}')
        
# create product object
nose_pin = Product('Dimond Nose Pin', 50, 31000)
# make purchases against different product quantities (make sure to run each test case)
nose_pin.make_purchase(2)
# do not forget to handle exceptions
# print the remaining stock after each purchase
print(f'Remaining Stock: {nose_pin.amount}')


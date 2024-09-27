def get_price():
    try:
        a = input("What do you want to purchase? ")
        quantity = int(input("How many do you want to purchase? "))

        if quantity <= 0:
            raise ValueError("You must purchase at least one item.")

        if quantity < 10:
            discount = 0
        elif 10 <= quantity < 100:
            discount = 10
        else:
            discount = 20

        # Summary output
        print(f"You purchased {quantity} {a}(s) and received a {discount}% discount.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
get_price()

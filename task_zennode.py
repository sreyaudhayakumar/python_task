class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
    def __init__(self,product,quantity):
        self.product={}
        self.quantity={}

    def add_product(self,product,quantity):
        self.product=product
        self.quantity=quantity

    def discount(self):
        total_quantity = sum(self.quantities.values())
        max_quantity = max(self.quantities.values())
        max_price = max(product.price for product in self.products.values())

        if total_quantity > 30 and max_quantity > 15:
            return "tiered_50_discount", 0.5 * max_price * (max_quantity - 15)
        elif total_quantity > 20:
            return "bulk_10_discount", 0.1 * sum(self.quantities[product] * self.products[product].price for product in self.products)
        elif max_quantity > 10:
            return "bulk_5_discount", 0.05 * max_price * max_quantity
        elif total_quantity > 200:
            return "flat_10_discount", 10
        else:
            return "no_discount", 0
        

    def fees(self):
        total_quantity=sum(self.quantities.values())
        package = total_quantity//10 + (total_quantity%10>0)
        shipping_fees_each = 5
        gift_wrap =1
        fees= package*shipping_fees_each
        gift_wrap_total= gift_wrap*total_quantity

        return fees,gift_wrap_total

    def display(self):
        print("Cart Contents:")
        for product_name, product in self.products.items():
            print(f"{product_name}: {self.quantities[product_name]} units, ${product.price} per unit")

        
        discount_name, discount_amount = self.discount()
        fees, gift_wrap_total = self.fees()

        print("\nDiscount Applied:")
        print(f"{discount_name} - ${discount_amount}")

        print("\nFees:")
        print(f"Shipping Fee: ${fees}")
        print(f"Gift Wrap Fee: ${gift_wrap_total}")

        
        total_amount = sum(self.quantities[product_name] * product.price for product_name, product in self.products.items()) - discount_amount + fees + gift_wrap_total
        print("\nTotal Amount:", total_amount)



product_a = Product("Product A", 20)
product_b = Product("Product B", 40)
product_c = Product("Product C", 50)

cart = Cart()
cart.add_product(product_a, 5)
cart.add_product(product_b, 10)
cart.add_product(product_c, 8)

cart.display()

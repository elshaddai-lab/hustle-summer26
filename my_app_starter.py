# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Elshaddai Manyahlhal
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Sneakers + slides
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be negative.")
        else:
            self.price = amount

# TICKET 5:
    def deliver(self):
        print("Shipping your sneakers!")


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
class Slide(Sneaker):
# TICKET 5: Each item's own action (Polymorphism continued)
    def deliver(self):
        print("Sliding out the door!")
# Explain: It can do this because it has all the attributes and methods of a Sneaker, but its own deliver method.


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: Air Max

item1 = Sneaker("Air Max", 120)
item2 = Slide("Cloud Slide", 45)

print(item1.name) 
# Predicted output: Air Max

# Break on purpose for Ticket 3:
item1.set_price(-5)
# Predicted output: The code will check if -5 is less than 0. Since it is true, it will print "No, price cannot be negative!" 
# Error message: # ValueError: Price cannot be negative. Price must be a positive number.


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added!")


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.
    def checkout(self):
        total = 0
    
        for item in self.items:
            item.deliver()
            total += item.price
        print("Total: $" +str(total))

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {"1": item1, "2": item2}
cart = Cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: It adds item1 ("Air Max") to the cartand prints "Air Max added!"
while True:
    choice = input("Pick 1, 2, or 'done' : ")
    if choice == "done":
        break
    elif choice in store:
        cart.add_item(store[choice])
    else:
        print("Invalid choice, try again.")
# Predicted output: When you pick 1: It adds item1 ("Air Max") to the cart and prints "Air Max added!"

# TICKET 10: Test the whole app
#   Run it start to finish.
cart.checkout()


# Predicted output: When you pick 1: It adds item1 ("Air Max") to the cart and prints "Air Max added!"
# Predicted output: When you pick 2: It adds item2 ("Cloud Slide") to the cart and prints "Cloud Slide added!"
# Predicted output: When you type "done": It will check out the cart and print the total.
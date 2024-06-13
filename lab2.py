"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item




# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class Inventory_Manager():
    def __init__(self,):
        self.items = []
    
    def add_Item (self, name, price, quantity):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                print(f"{name}already added")               
                return False
        item = Item(name, price, quantity) 
        self.items.append(item)
        print(f"Item added: {name}")
        return True    
    
    def remove_Item(self, name):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                self.items.remove(existing_item)
                return True
        return False
    
    def update_price(self, name, price):
        for existing_item in self.items:
            if existing_item.get_name() == name:
                existing_item.set_price(price)  # Update the price
                return True
        return False

    def display(self):
        for item in self.items:
            print(f"item name: {item.get_name()}, price: ${item.get_price()}, quantity: {item.get_quantity()}")

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.
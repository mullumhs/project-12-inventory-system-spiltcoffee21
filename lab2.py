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
from lab1 import item




# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.
class Inventory_Manager():
    def __init__(self,):
        self.item = []
    
    def add_item (self, item):
        for existing_item in self.item:
            if existing_item.get_name() == item.get_item():
                return false
        self.item.append(item)
        return True
    
    def remove_item():
        for i, existing_item in (self.item):
            if existing_item.get_name() == item.get_item():
                
        
    def update_item():
                
        
        
        
    




# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.




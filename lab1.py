"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.
class Item():
    def __init__(self, name, price, quantity):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity( quantity)
         




# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.
    def get_name(self):
        return self._name




# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.
    def set_name(self, name):
        if name == "":
            raise ValueError("name the name")
        self._name = name




# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.
 
    def get_price(self):
        return self._price





# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.
    def set_price(self, price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self._price = price
        




# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.
    def get_quantity(self):
        return self._quantity





# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.
def set_quantity(self, quantity):
    if quantity < 0:
        raise ValueError ("quantity cannot be negative")
    self._quantity = quantity




# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.
fish = Item("fish", 5000000000000, 1)
apple = Item("", 7, 43)
paper = Item("paper", 600, -5)
water = Item("water", -5, -30 )






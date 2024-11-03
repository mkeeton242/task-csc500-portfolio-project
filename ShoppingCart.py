###
# Project:      ShoppingCart.py
# Author:       Michael Keeton
# Created:      10/20/2024
# Description:  Creates the ShoppingCart class.
###

import ItemToPurchase as itp

# Create the ShoppingCart class.
class ShoppingCart:
    
    # constructor function
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    # Adds an item to cart_items list.
    def add_item(self, item):
        self.cart_items.append(item)
    
    # Removes item from cart_items list.
    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
        else:
            print('Item not found in cart. Nothing removed.')
    
    # Modifies an item's description, price, and/or quantity.
    def modify_item(self, temp_item):
        if temp_item.item_name in self.cart_items:
            item_index = self.cart_items.index(temp_item.item_name)
            item = self.cart_items[item_index]
            if temp_item.item_price != 0:
                item.item_price = temp_item.item_price
            if temp_item.item_quantity != 0:
                item.item_quantity = temp_item.item_quantity
            if temp_item.item_description != '':
                item.item_description = temp_item.item_description
        else:
            print('Item not found in cart. Nothing modified.') 
    
    # Returns quantity of all items in cart.
    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for item in self.cart_items:
            num_items_in_cart += item.item_quantity
        
        return int(num_items_in_cart)
    
    # Determines and returns the total cost of items in cart.
    def get_cost_of_cart(self):
        cost_of_cart = 0.0
        for item in self.cart_items:
            cost_of_cart += item.item_quantity * item.item_price
        
        return float(cost_of_cart)
    
    # Outputs total of objects in cart.
    def print_total(self):
        if len(self.cart_items) > 0:
            print(f'{self.customer_name:s}\'s Shopping Cart - {self.current_date:s}')
            print(f'Number of Items: {self.get_num_items_in_cart():d}')
            for item in self.cart_items:
                item.print_item_cost()
            print(f'Total: ${self.get_cost_of_cart():.2f}')
        else:
            print('SHOPPING CART IS EMPTY')
    
    # Outputs each item's description.
    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print(f'{self.customer_name:s}\'s Shopping Cart - {self.current_date:s}')
            print('Item Descriptions')
            for item in self.cart_items:
                print(f'{item.item_name:s}: {item.item_description:s}')

# Adds an item to the shopping cart.
def menu_add_item(shopping_cart):
    print('ADD ITEM TO CART')
    new_item = itp.item_prompt()
    shopping_cart.add_item(new_item)

# Removes an item from the shopping cart.
def menu_remove_item(shopping_cart):
    print('REMOVE ITEM FROM CART')
    item_name = input('Enter name of item to remove:\n')
    shopping_cart.remove_item(item_name)

# Changes the quantity of an item in the shopping cart.
def menu_change_item_qty(shopping_cart):
    print('CHANGE ITEM QUANTITY')
    item_name = input('Enter the item name:\n')
    item_quantity = int(input('Enter the new quantity:\n'))
    modified_item = itp.ItemToPurchase(item_name, 0, item_quantity, "")
    shopping_cart.modify_item(modified_item)

# Output the items' descriptions from the shopping cart.
def menu_output_descriptions(shopping_cart):
    print('OUTPUT ITEMS\' DESCRIPTIONS')
    shopping_cart.print_descriptions()

# Output the items from the shopping cart.
def menu_output_shopping_cart(shopping_cart):
    print('OUTPUT SHOPPING CART')
    shopping_cart.print_total()

# Outputs a menu of options to manipulate the shopping cart.
def print_menu(shopping_cart):
    menu_string = 'MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit'
    print(menu_string)
    menu_option = input('Choose an option: ')
    
    while menu_option != 'q':
        if menu_option == 'i':
            menu_output_descriptions(shopping_cart)
        elif menu_option == 'o':
            menu_output_shopping_cart(shopping_cart)
        elif menu_option == 'a':
            menu_add_item(shopping_cart)
        elif menu_option == 'r':
            menu_remove_item(shopping_cart)
        elif menu_option == 'c':
            menu_change_item_qty(shopping_cart)
        else:
            print('INVALID INPUT')
        
        print(menu_string)
        menu_option = input('Choose an option: ')
        
def main():
    shopping_cart = ShoppingCart('John Doe', 'February 1, 2020')
    shopping_cart.add_item(itp.ItemToPurchase('Nike Romaleos', 189, 2, 'Volt color, Weightlifting shoes'))
    shopping_cart.add_item(itp.ItemToPurchase('Chocolate Chips', 3, 5, 'Semi-sweet'))
    shopping_cart.add_item(itp.ItemToPurchase('Powerbeats 2 Headphones', 128, 1, 'Bluetooth headphones'))
    print_menu(shopping_cart)
    
if __name__ == "__main__":
    main()

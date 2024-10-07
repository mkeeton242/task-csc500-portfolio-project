###
# Project:      ItemToPurchase.py
# Author:       Michael Keeton
# Created:      09/30/2024
# Description:  Creates the ItemToPurchase class.
###

# Create the ItemToPurchase class.
class ItemToPurchase:
    
    # constructor function
    def __init__(self, item_name = "", item_price = float(0), item_quantity = int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    # Prints the attributes of the object.
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print('{:s} {:d} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, item_total))

# Prompts the user for the inputs to create an ItemToPurchase object.
def item_prompt():
    
    item_name = input('Enter the item name: ')
    item_price = float(input('Enter the item price: '))
    item_quantity = int(input('Enter the item quantity: '))
    new_item = ItemToPurchase(item_name, item_price, item_quantity)
    return new_item

def main():
    # Prompts the user for two items and creates two ItemToPurchase objects.
    print('Item 1')
    item1 = item_prompt()
    
    print('Item 2')
    item2 = item_prompt()
    
    # Add the costs of the items together and output the total cost.
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    items_total = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print('Total: ${:.2f}'.format(items_total))

main()
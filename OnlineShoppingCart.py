###
# Project:      OnlineShoppingCart.py
# Author:       Michael Keeton
# Created:      10/23/2024
# Description:  User enters a course number and displays the course's
#               room number, instructor, and meeting time.
###

import ShoppingCart as sc

def main():
    
    # Prompt the user for a customer's name and today's date
    customer_name = input('Enter customer\'s name: ')
    date = input('Enter today\'s date: ')
    
    # Output the name and date.
    print('Customer name:', customer_name)
    print('Today\'s date:', date)
    shopping_cart = sc.ShoppingCart(customer_name, date)
    sc.print_menu(shopping_cart)

if __name__ == "__main__":
    main()
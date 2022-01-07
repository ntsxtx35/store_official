from utils import clear
import add_info
import placing_order
import file_IO
import list_item_info
import promotion
import list_customer_info
import search_items
import filter_by_genre

# Read input file
items_dict = file_IO.read_file_create_dict('item.txt')
customers_dict = file_IO.read_file_create_dict('customer.txt')


def print_menu():
    print(f'1. List all items \n'
          f'2. List all info of a specific item \n'
          f'3. Search item by name \n'
          f'4. Search item by item id \n'
          f'5. List all info of a specific customer\n'
          f'6. Placing orders\n'
          f'7. Add item/customer information\n'
          f'8. Promote\n'
          f'9. Filter items by genre\n'
          f'0. Exit')


print_menu()
choice = 1
while choice:
    choice = int(input('Enter a number to select a feature: '))
    if choice == 1:
        list_item_info.list_item(items_dict)
    elif choice == 2:
        list_item_info.list_item(items_dict)
        item_id = input('Enter item ID: ')
        list_item_info.list_item_info(items_dict, item_id)
    elif choice == 3:
        search_items.search_name(items_dict)
    elif choice == 4:
        search_items.search_id(items_dict)
    elif choice == 5:
        customer_id = input('Enter customer id: ')
        customer_id = placing_order.check_user_customer_input(customer_id, customers_dict)
        list_customer_info.list_cus(customers_dict, customer_id)
    elif choice == 6:
        order_list, total, cus_id = placing_order.placing_order(items_dict, customers_dict)
        placing_order.bill(order_list, customers_dict, items_dict, total, cus_id)
    elif choice == 7:
        add = input("Enter 'item' to add item and 'cus' to add customer: ")
        if add == 'item':
            add_info.add_items(items_dict)
        else:
            customer_id = input('Enter customer id: ')
            while customer_id in customers_dict:
                new_customer_id = input('Please input the ID again: ')
                customer_id = new_customer_id
            add_info.add_customers(customers_dict, customer_id)
    elif choice == 8:
        promotion.promote(customers_dict)
    elif choice == 9:
        filter_by_genre.choose_genre(items_dict)
    else:
        print('Invalid option')
    choice = int(input('Press any number to continue, 0 to stop '))
    if choice:
        clear()
        print_menu()

file_IO.write_to_file(items_dict, 'item.txt')
file_IO.write_to_file(customers_dict, 'customer.txt')

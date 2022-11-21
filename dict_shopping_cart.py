def show_item(shopping_cart, quantity):
    total = 0
    for key, val in shopping_cart.items():
        # Formula for finding the total of the items in grocery cart
        item_total = val['quantity'] * val['price']
        # Adding current total to the new additional total
        total += item_total
        # :.2f gives the item total 2 decimal points
        # format function: key refers to name of item, quantity refers to val of the key quantity, item_total equals item_total formula ealier in defined function
        # format function allows us to insert values inside the {}
        print(f"{key} x {quantity} = {item_total:.2f}".format(key=key.title(), quantity=val['quantity'], item_total=item_total))
    print(f"Total: ${total:.2f}")

def add_item(shopping_cart, name, quantity, price):
    # This defined function is adding item that already exist in the dictionary
    if name in shopping_cart:
        while True:
            choice = input(f"Looks like {name} is already included in our cart. Would you like to update how much of {name} you would like in your cart? :")
            
            if choice == 'y' or 'yes':
                shopping_cart[name]['quantity'] += quantity
                break

            elif choice == 'n' or 'no':
                print("Okay, cancelling item update...")
                break
            else:
                print("This selection does not exit in your cart. Try again.")
    else:
        shopping_cart[name] = {
            'quantity': quantity,
            'price': price
        }
        print(f"{name} has been added to your cart.".format(name=name.title()))


def delete_item(shopping_cart, name):
    if name in shopping_cart:
        del shopping_cart[name]
    else:
        print(f"{name} does not show to be in your cart.".format(name))


def main():
    shopping_cart = {}

    application_running = True
    while application_running:
        main_choices = input("Hello, what would you like to do today? (A)dd item to cart | (D)elete item in your cart | (S)how item(s) in your cart | (Q)uit program : ").lower()

        if main_choices == 'a' or 'add':
            name = input("What item would you like to add to your cart?\n:")
            quantity = input(f"How much {name} would you like to add to your cart?\n:")
            price = (float(input(f"How much does {name} cost?\n:$")))

            add_item(shopping_cart, name, quantity, price)

        elif main_choices == 'd' or 'delete':
            name = input("What would you like to delete?").lower()

            delete_item(shopping_cart, name)

        elif main_choices == 's' or 'show':
            show_item(shopping_cart)

        elif main_choices == 'q' or 'quit':
            print("Thank you for shopping with us! Below is your receipt for your groceries...")
            show_item(shopping_cart)
            application_running = False

        input("Press (ENTER) to continue...")

    
print(main())
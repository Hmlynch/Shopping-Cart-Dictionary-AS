shopping_cart = {}

def add_item(name, quantity):
    if name in shopping_cart.keys():
        shopping_cart[name] += quantity
    else:
        shopping_cart[name] = quantity

def delete_item(name, quantity):
    if name not in shopping_cart.keys():
        print(f"{name} does not show to be in your shopping cart at the moment.")
    else:
        shopping_cart[name] -= quantity
        if name in shopping_cart and shopping_cart[name] <= 0:
            del shopping_cart[name]

def main():
    application_running = True
    while application_running:
        main_prompt = input("What would you like to do? (A)dd item | (D)elete item | (S)how item :").lower()

        if main_prompt == 'a' or main_prompt == 'add':
            name = input("What is the item you would like to add to your cart? :").lower()
            quantity = int(input(f"How much {name} would you like to add? :"))
            add_item(name, quantity)

        elif main_prompt == 'd' or main_prompt == 'delete':
            name = input("What item would you like to remove from your cart?").lower()
            quantity = int(input(f"How much {name} would you like to remove"))
            delete_item(name, quantity)
        
        elif main_prompt == 's' or main_prompt == 'show':
            print(f"Here is your cart at the moement:\n {shopping_cart}")

        else:
            print(f"'{main_prompt}' is not a valid option. Please selelect (A)dd item | (D)elete item | (S)how item :")

        while True:
            quit_prompt = input("Would you like to coninue? (Y)es | (N)o :").lower()

            if quit_prompt == 'y' or quit_prompt == 'yes':
                break

            elif quit_prompt == 'n' or quit_prompt == 'no':
                print(f"Thank you for shopping with us! Here is your reciept:\n {shopping_cart}")
                application_running = False
                break

            else:
                print(f"'{quit_prompt}' is not a valid option. Please select (Y)es | (N)o :")

main()
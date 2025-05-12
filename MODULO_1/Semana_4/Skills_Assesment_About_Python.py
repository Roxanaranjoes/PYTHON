"""

Skills Assesment About Ṕython
 
----Store Inventory Management System----

Overview:
This system is designed for managing a store's inventory, allowing the user to interact and have a clear perspective of what is currently in the store. It also has a main menu that is designed so that the user can navigate through the different options that the program has.

Features:
 -The system has the following features that allow you to do:
1. Add Products to Inventory: Allows the user to add products with attributes such as name, price, and available quantity.
2. Query Products in Inventory: Search for a product by name and display its details (name, price, quantity).
3. Update Product Prices: Change the price of a specific product in inventory.
4. Remove Products from Inventory: Allows the user to remove a product that is no longer available.
5. Calculate Total Inventory Value: Multiply the price by the quantity of each product and display the running total.

Instructions for running the program:
 -Interactive menu:Initially, when running the program it displays an interactive menu so that the user can select what to do.
 -Add a new product ("add" function):
The first option will allow you to add a new product to your inventory. If the product exists, it updates the quantity of the product in your inventory.
   -It prompts the user for the following information:
1. The name of the product.
2. The quantity of the product.
3. The price of the product.
 -Search for a product ("search" function):
The second option asks the user for the product name, and if the product is not found, it tells them that it has not been found. If it is, it displays details about it (quantity, price).
 -Update a product's price ("Update" function):
The third option initially asks the user for the name of the product whose price they wish to update. If the product is not in inventory, a message is displayed informing them. If the product is in inventory, it shows the current price and asks for the new price.
 -Delete product (Delete function):
The fourth option asks the user for the name of the product they wish to delete. If the product does not exist, a message appears stating that the product was not entered. If it exists, the user is asked again if they wish to delete it. If the answer is yes, the user deletes it. If not, the product remains in the inventory.
 -Calculate Total Inventory Value ("calculate" function):
 The fifth option calculates the total value of the inventory, taking into account the products, their quantities and their prices.
 -Exit:The last option ends the system.

Programming language: Python
 

Author: Roxana Naranjo Estrada




"""




print("\nWelcome to the Store Inventory Management System📦")

# Initial inventory setup
inventory = [
    {"name": "Milk", "price": 255, "quantity": 85},
    {"name": "Apple", "price": 85, "quantity": 42},
    {"name": "Cake", "price": 56, "quantity": 37},
    {"name": "Butter", "price": 62, "quantity": 33},
    {"name": "Sugar", "price": 75, "quantity": 22}
]

# Function to check if the input is a valid positive number
def is_valid_number(value):
    try:
        return float(value.strip()) > 0
    except ValueError:
        return False

# Add a new product in the inventory
def add_product(name, price, quantity):
    for product in inventory:
        if product["name"].strip().title() == name.strip().title():
            print("🔁 Product already exists in the inventory. Updating the quantity.")
            product["quantity"] += quantity
            return
    inventory.append({"name": name.strip().title(), "price": price, "quantity": quantity})
    print(f"✅ Product '{name}' has been added successfully.")

# Function to search for a product by its name
def search_product(name):
    for product in inventory:
        if product["name"].strip().title() == name.strip().title():
            return product
    return None

# Function to update the price of a product
def update_price(name, new_price):
    product = search_product(name)
    if not product:
        print("❌ Product not found in the inventory.")
        return
    if is_valid_number(str(new_price)):
        product["price"] = float(new_price)
        print(f"💲 Price of '{name}' has been updated to ${new_price}.")
    else:
        print("❌⚠️ Invalid price. Price must be a positive number.")

# Function to delete a product
def delete_product(name):
    product = search_product(name)
    if not product:
        print("❌ Product not found in the inventory.")
        return

    print(f"📝 Product found: Name: {product['name']}, Price: 💲{product['price']}, Quantity: {product['quantity']}")
    delete_choice = input("Do you want to delete the product? (yes/no): ").strip().lower()
    while delete_choice not in ("yes", "no"):
        delete_choice = input("⚠️ Please type 'yes' or 'no': ").strip().lower()
    if delete_choice == "yes":
        inventory.remove(product)
        print(f"🗑️ Product '{name}' has been removed from the inventory.")
    else:
        print(f"ℹ️ Product '{name}' remains in inventory.")

# Function to calculate the total value of the inventory in the store
def calculate_inventory_value():
    total_value = sum(product["price"] * product["quantity"] for product in inventory)
    return total_value

# Function to display the menu and get user choice
def show_menu():
    print("\n📦 Inventory Management Menu:")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
    return input("\nChoose an option (1-6): ").strip()

# Main function to run the inventory manager and handle options
def run_inventory_manager():
    while True:
        option = show_menu()

        match option:
            case "1":
                name = input("Enter the product name: ").strip().title()
                product = search_product(name)
                if product:
                    quantity_input = input("Enter the quantity to add: ").strip()
                    if quantity_input.isdigit() and int(quantity_input) > 0:
                        add_product(name, 0, int(quantity_input))
                    else:
                        print("❌ Quantity must be a positive number.")
                else:
                    try:
                        quantity = int(input("Enter the product quantity: ").strip())
                        price = float(input("Enter the product price: ").strip())
                        if quantity > 0 and price > 0:
                            add_product(name, price, quantity)
                        else:
                            print("❌ Price and quantity must be greater than 0.")
                    except ValueError:
                        print("❌ Invalid input. Price and quantity must be numbers.")

            case "2":
                name = input("\nEnter the product name to search: ").strip().title()
                product = search_product(name)
                if product:
                    print(f"✅ Product found: Name: {product['name']}, Price: 💲{product['price']}, Quantity: {product['quantity']}")
                else:
                    print("❌ Product not found in the inventory.")

            case "3":
                name = input("\nEnter the product name to update price: ").strip().title()
                product = search_product(name)
                if not product:
                    print("❌ Product not found in the inventory.")
                else:
                    print(f"\n💲 Current price: {product['price']}")
                    new_price = input("Enter the new price: ").strip()
                    update_price(name, new_price)

            case "4":
                name = input("\nEnter the product name to delete: ").strip().title()
                delete_product(name)

            case "5":
                total_value = calculate_inventory_value()
                print(f"\n💰 Total value of the inventory: ${total_value:.2f}")

            case "6":
                print("\nExiting the program. Goodbye! 👋")
                break

            case _:
                print("⚠️ Invalid option. Please choose a number between 1 and 6.")

# Start the inventory manager program
run_inventory_manager()

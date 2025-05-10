# 📦 Inventory Manager
print("Welcome to the Inventory Manager!")

# Global inventory list, each product is a dictionary
inventory = []
errors = 0  # Counter for invalid inputs (max 5)

# Lambda to check if a string is a valid number (positive)
is_valid_number = lambda s: s.replace('.', '', 1).isdigit() and float(s) >= 0

# Lambda to calculate total inventory value
calculate_inventory_value = lambda: sum(p["price"] * p["quantity"] for p in inventory)

# Add a new product or update an existing one
def add_product(name, price, quantity):
    for product in inventory:
        if product["name"] == name:
            product["quantity"] += quantity
            product["price"] = price
            print(f"🔁 Updated product: {name}")
            return
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"✅ Added product: {name}")

# Find a product by name
def find_product(name):
    for product in inventory:
        if product["name"] == name:
            return product
    return None

# Update the price of an existing product
def update_product_price(name, new_price):
    product = find_product(name)
    if product:
        product["price"] = new_price
        print(f"💲 Updated price for: {name}")
    else:
        print("❌ Product not found.")

# Delete a product by name
def delete_product(name):
    for i in range(len(inventory)):
        if inventory[i]["name"] == name:
            del inventory[i]
            print(f"🗑️ Deleted product: {name}")
            return
    print("❌ Product not found.")

# Show the main menu
def show_menu():
    print("\n📋 MENU")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product Price")
    print("4. Delete Product")
    print("5. Show Total Inventory Value")
    print("6. Exit")
    return input("Choose an option (1–6): ").strip()

# Main program loop (with match-case and error control)
def run_inventory_manager():
    global errors
    for _ in range(100):  # Limit to 100 interactions to avoid infinite loop
        if errors >= 5:
            print("🚫 Too many invalid attempts. Exiting program.")
            return

        option = show_menu()

        match option:
            case "1":
                name = input("Enter product name: ").strip().lower()
                price = input("Enter price: ")
                quantity = input("Enter quantity: ")
                if is_valid_number(price) and quantity.isdigit():
                    add_product(name, float(price), int(quantity))
                else:
                    errors += 1
                    print(f"⚠️ Invalid input. Errors: {errors}/5")

            case "2":
                name = input("Enter product name to search: ").strip().lower()
                product = find_product(name)
                if product:
                    print(f"🔍 {name.capitalize()} — Price: ${product['price']}, Quantity: {product['quantity']}")
                else:
                    print("❌ Product not found.")

            case "3":
                name = input("Enter product name to update price: ").strip().lower()
                new_price = input("Enter new price: ")
                if is_valid_number(new_price):
                    update_product_price(name, float(new_price))
                else:
                    errors += 1
                    print(f"⚠️ Invalid price. Errors: {errors}/5")

            case "4":
                name = input("Enter product name to delete: ").strip().lower()
                delete_product(name)

            case "5":
                total = calculate_inventory_value()
                print(f"💰 Total inventory value: ${total:.2f}")

            case "6":
                print("👋 Exiting the program. Goodbye!")
                return

            case _:
                errors += 1
                print(f"❌ Invalid option. Errors: {errors}/5")

# Start the inventory management system
run_inventory_manager()

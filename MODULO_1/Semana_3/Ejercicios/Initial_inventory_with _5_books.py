# Initial inventory with 5 books
inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

# Error counter
errors = 0
max_errors = 10

# Function to print the inventory
def print_inventory():
    print("\n📚 Current Inventory:")
    if not inventory:
        print("No books in inventory.")
    else:
        for i, book in enumerate(inventory, 1):
            print(f"{i}. Title: {book['title']} | Price: ${book['price']} | Quantity: {book['quantity']}")
    print()

# Function to add a book to the inventory
def add_book():
    global errors
    title = input("Enter book title: ").strip()
    price_input = input("Enter price: ")
    quantity_input = input("Enter quantity: ")

    if price_input.replace('.', '', 1).isdigit() and quantity_input.isdigit():
        price = float(price_input)
        quantity = int(quantity_input)

        if price > 0 and quantity > 0:
            inventory.append({"title": title, "price": price, "quantity": quantity})
            print("✅ Book added.")
        else:
            print("❌ Price and quantity must be positive numbers.")
            errors += 1
    else:
        print("❌ Invalid input. Price must be a number and quantity must be an integer.")
        errors += 1

# Function to search a book by title
def search_book():
    global errors
    title = input("Enter title to search: ").strip()
    found = False
    for book in inventory:
        if book['title'].lower() == title.lower():
            print(f"📘 Found: {book['title']} | Price: ${book['price']} | Quantity: {book['quantity']}")
            found = True
            break
    if not found:
        print("❌ Book not found in inventory.")
        errors += 1

# Function to update the price of a book
def update_price():
    global errors
    title = input("Enter title to update: ").strip()
    new_price_input = input("Enter new price: ")

    if new_price_input.replace('.', '', 1).isdigit():
        new_price = float(new_price_input)
        if new_price > 0:
            found = False
            for book in inventory:
                if book['title'].lower() == title.lower():
                    book['price'] = new_price
                    print("✅ Price updated.")
                    found = True
                    break
            if not found:
                print("❌ Book not found.")
                errors += 1
        else:
            print("❌ Price must be positive.")
            errors += 1
    else:
        print("❌ Invalid price format.")
        errors += 1

# Function to update the quantity of a book
def update_quantity():
    global errors
    title = input("Enter title to update quantity: ").strip()
    new_quantity_input = input("Enter new quantity: ")

    if new_quantity_input.isdigit():
        new_quantity = int(new_quantity_input)
        if new_quantity >= 0:
            found = False
            for book in inventory:
                if book['title'].lower() == title.lower():
                    book['quantity'] = new_quantity
                    print("✅ Quantity updated.")
                    found = True
                    break
            if not found:
                print("❌ Book not found.")
                errors += 1
        else:
            print("❌ Quantity must be a non-negative integer.")
            errors += 1
    else:
        print("❌ Invalid quantity format.")
        errors += 1

# Function to delete a book from inventory
def delete_book():
    global errors
    title = input("Enter title to delete: ").strip()
    found = False
    for i, book in enumerate(inventory):
        if book['title'].lower() == title.lower():
            del inventory[i]
            print("🗑️ Book deleted.")
            found = True
            break
    if not found:
        print("❌ Book not found in inventory.")
        errors += 1

# Function to calculate the total value of the inventory
def calculate_total_value():
    total_value = sum((lambda b: b['price'] * b['quantity'])(book) for book in inventory)
    print(f"💰 Total Inventory Value: ${total_value:.2f}")

# Function to handle the main menu and user input
def main():
    global errors
    running = True
    while running and errors < max_errors:
        print("\n=== Bookstore Inventory Management ===")
        print("1. Add book")
        print("2. Search book")
        print("3. Update book price")
        print("4. Update book quantity")  # New option to update quantity
        print("5. Delete book")
        print("6. Calculate total value")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        match choice:
            case "1":
                add_book()
            case "2":
                search_book()
            case "3":
                update_price()
            case "4":
                update_quantity()  # Handle update quantity option
            case "5":
                delete_book()
            case "6":
                calculate_total_value()
            case "7":
                print("👋 Exiting the program.")
                running = False
            case _:
                print("❌ Invalid option.")
                errors += 1

        # Check if the number of errors reached the limit
        if errors >= max_errors:
            print("\n🚫 Too many invalid inputs. Program terminated.")
            running = False

# Run the main function to start the program
if __name__ == "__main__":
    main()


# 📚 Library Inventory Management System

# Initial inventory setup
inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

# Function to check if the input is a valid positive number
def is_valid_number(value):
    return value.replace('.', '', 1).isdigit() and float(value) > 0

# Function to add a book to the inventory
def add_book(title, price, quantity):
    for book in inventory:
        if book["title"].lower() == title.lower():
            print("Error 1: Book already exists in the inventory. Updating the quantity.")
            book["quantity"] += quantity
            return
    inventory.append({"title": title, "price": price, "quantity": quantity})
    print(f"Book '{title}' has been added successfully.")

# Function to search for a book by its title
def search_book(title):
    for book in inventory:
        if book["title"].lower() == title.lower():
            return book
    return None

# Function to update the price of a book
def update_price(title, new_price):
    book = search_book(title)
    if book and is_valid_number(str(new_price)):
        book["price"] = new_price
        print(f"Price of '{title}' has been updated to ${new_price:.2f}.")
    elif not book:
        print("Error 2: Book not found in the inventory.")
    else:
        print("Error 3: Invalid price. Price must be a positive number.")

# Function to delete a book from the inventory
def delete_book(title):
    book = search_book(title)
    if book:
        inventory.remove(book)
        print(f"Book '{title}' has been removed from the inventory.")
    else:
        print("Error 4: Book not found in the inventory.")

# Function to calculate the total value of the inventory
def calculate_inventory_value():
    total_value = sum(book["price"] * book["quantity"] for book in inventory)
    return total_value

# Function to display the menu and get user choice
def show_menu():
    print("\n📚 Inventory Management Menu:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Update Book Price")
    print("4. Delete Book")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
    return input("Choose an option (1-6): ").strip()

# Main function to run the inventory manager and handle options
def run_inventory_manager():
    while True:
        option = show_menu()

        match option:
            case "1":
                title = input("Enter the book title: ").strip()
                price = input("Enter the book price: ")
                quantity = input("Enter the book quantity: ")
                
                if is_valid_number(price) and quantity.isdigit():
                    add_book(title, float(price), int(quantity))
                else:
                    print("Error 5: Invalid input. Price and quantity must be positive numbers.")
                    
            case "2":
                title = input("Enter the book title to search: ").strip()
                book = search_book(title)
                if book:
                    print(f"Book found: Title: {book['title']}, Price: ${book['price']}, Quantity: {book['quantity']}")
                else:
                    print("Error 6: Book not found in the inventory.")
                    
            case "3":
                title = input("Enter the book title to update price: ").strip()
                new_price = input("Enter the new price: ")
                update_price(title, new_price)

            case "4":
                title = input("Enter the book title to delete: ").strip()
                delete_book(title)

            case "5":
                total_value = calculate_inventory_value()
                print(f"Total value of the inventory: ${total_value:.2f}")
                
            case "6":
                print("Exiting the program. Goodbye!")
                break
                
            case _:
                print("Error 7: Invalid option. Please choose a number between 1 and 6.")

# Start the inventory manager program
run_inventory_manager()

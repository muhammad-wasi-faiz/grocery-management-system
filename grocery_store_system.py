"""Smart Grocery Store Management System.

A console application that manages products (list of dictionaries),
stock updates, customer sales and a final store report.
"""

LOW_STOCK_LIMIT = 5

# Starter data so the system can be demonstrated immediately.
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 4},
    {"id": 103, "name": "Rice", "category": "Grains", "price": 480, "stock": 50},
]

# Separate list that records every completed sale.
sales_records = []


# ---------- Input helper functions ----------

def get_int(prompt, min_value=0):
    # Ask until the user enters a whole number >= min_value.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if value >= min_value:
            return value
        print(f"  Value must be at least {min_value}.")


def get_price(prompt):
    # Ask until the user enters a number greater than zero.
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 250 or 99.5).")
            continue
        if value > 0:
            return value
        print("  Price must be greater than 0.")


def get_text(prompt):
    # Ask until the user enters non-empty text; returns it cleaned and title-cased.
    while True:
        text = input(prompt).strip().title()
        if text:
            return text
        print("  This field cannot be empty.")


# ---------- Product lookup helpers ----------

def find_product_by_id(product_id):
    # Return the product dictionary with this ID, or None if not found.
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def print_product(product):
    # Print the full details of one product.
    print(f"  ID       : {product['id']}")
    print(f"  Name     : {product['name']}")
    print(f"  Category : {product['category']}")
    print(f"  Price    : Rs. {product['price']:.2f}")
    print(f"  Stock    : {product['stock']} units")


# ---------- Menu operations ----------

def add_product():
    # Collect product info, reject duplicate IDs, then append the new dictionary.
    print("\n--- Add New Product ---")
    product_id = get_int("Enter product ID: ", min_value=1)
    if find_product_by_id(product_id) is not None:
        print("  Error: a product with this ID already exists.")
        return
    new_product = {
        "id": product_id,
        "name": get_text("Enter product name: "),
        "category": get_text("Enter category: "),
        "price": get_price("Enter price: "),
        "stock": get_int("Enter available stock: "),
    }
    products.append(new_product)
    print(f"  '{new_product['name']}' added successfully.")


def view_products():
    # Display all products in a table.
    print("\n--- All Products ---")
    if not products:
        print("  No products available.")
        return
    print(f"{'ID':<8}{'Name':<18}{'Category':<14}{'Price':>10}{'Stock':>8}")
    print("-" * 58)
    for product in products:
        print(f"{product['id']:<8}{product['name']:<18}{product['category']:<14}"
              f"{product['price']:>10.2f}{product['stock']:>8}")


def search_product():
    # Search by ID (digits) or by name (case-insensitive, partial match allowed).
    print("\n--- Search Product ---")
    query = input("Enter product name or ID: ").strip()
    if not query:
        print("  Search cannot be empty.")
        return
    found = []
    for product in products:
        if query.isdigit() and product["id"] == int(query):
            found.append(product)
        elif query.lower() in product["name"].lower():
            found.append(product)
    if not found:
        print(f"  No product found matching '{query}'.")
        return
    for product in found:
        print()
        print_product(product)


def update_stock():
    # Add to a product's stock or overwrite its quantity.
    print("\n--- Update Product Stock ---")
    product_id = get_int("Enter product ID: ", min_value=1)
    product = find_product_by_id(product_id)
    if product is None:
        print("  Product not found.")
        return
    print(f"  {product['name']} currently has {product['stock']} units.")
    print("  1. Add stock")
    print("  2. Set exact quantity")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        amount = get_int("Enter quantity to add: ", min_value=1)
        product["stock"] += amount
    elif choice == "2":
        product["stock"] = get_int("Enter new stock quantity: ", min_value=0)
    else:
        print("  Invalid option. No changes made.")
        return
    print(f"  Updated stock for {product['name']}: {product['stock']} units.")


def process_sale():
    # Validate the sale, deduct stock, record it, and print a summary.
    print("\n--- Process Customer Sale ---")
    product_id = get_int("Enter product ID: ", min_value=1)
    product = find_product_by_id(product_id)
    if product is None:
        print("  Product not found.")
        return
    quantity = get_int(f"Enter quantity for {product['name']}: ", min_value=1)
    if quantity > product["stock"]:
        print(f"  Sale denied: only {product['stock']} units in stock.")
        return

    total = quantity * product["price"]
    product["stock"] -= quantity   # deduct sold units from inventory

    # Store the completed sale as a dictionary in the sales list.
    sales_records.append({
        "id": product["id"],
        "name": product["name"],
        "quantity": quantity,
        "total": total,
    })

    print("\n  ----- Purchase Summary -----")
    print(f"  Product        : {product['name']}")
    print(f"  Quantity       : {quantity}")
    print(f"  Unit price     : Rs. {product['price']:.2f}")
    print(f"  Total amount   : Rs. {total:.2f}")
    print(f"  Stock remaining: {product['stock']}")


def view_sales():
    # Display every recorded sale.
    print("\n--- Sales Records ---")
    if not sales_records:
        print("  No sales recorded yet.")
        return
    print(f"{'No.':<6}{'ID':<8}{'Product':<18}{'Qty':>6}{'Total':>12}")
    print("-" * 50)
    for number, sale in enumerate(sales_records, start=1):
        print(f"{number:<6}{sale['id']:<8}{sale['name']:<18}"
              f"{sale['quantity']:>6}{sale['total']:>12.2f}")


def generate_report():
    # Show store-wide statistics.
    print("\n" + "=" * 40)
    print("STORE REPORT")
    print("=" * 40)

    total_stock = 0
    for product in products:
        total_stock += product["stock"]

    total_revenue = 0
    for sale in sales_records:
        total_revenue += sale["total"]

    print(f"Total products          : {len(products)}")
    print(f"Total available stock   : {total_stock}")
    print(f"Total sales transactions: {len(sales_records)}")
    print(f"Total revenue           : Rs. {total_revenue:.2f}")

    print(f"\nProducts with stock below {LOW_STOCK_LIMIT}:")
    low_found = False
    for product in products:
        if product["stock"] < LOW_STOCK_LIMIT:
            print(f"  {product['name']} (ID {product['id']}) - {product['stock']} left")
            low_found = True
    if not low_found:
        print("  None")

    if products:
        highest = max(product["price"] for product in products)
        lowest = min(product["price"] for product in products)
        # List every product at the extreme price so ties are shown.
        print("\nHighest priced product(s):")
        for product in products:
            if product["price"] == highest:
                print(f"  {product['name']} - Rs. {highest:.2f}")
        print("Lowest priced product(s):")
        for product in products:
            if product["price"] == lowest:
                print(f"  {product['name']} - Rs. {lowest:.2f}")
    print("=" * 40)


def show_menu():
    # Print the main menu.
    print("\n" + "=" * 36)
    print("SMART GROCERY STORE SYSTEM")
    print("=" * 36)
    print("\n1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")


def main():
    # Run the menu loop until the user chooses Exit.
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("\nThank you for using the Smart Grocery Store System. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()

# Smart Grocery Store Management System

## Overview
A console-based Python application that helps a local grocery store owner manage
products, stock, customer sales and reports. It uses **lists of dictionaries** as
its main data structures and runs from a menu until the user chooses to exit.

## Features
1. **Add New Product** - stores a product dictionary with `.append()`; duplicate IDs are rejected.
2. **View All Products** - shows ID, name, category, price and stock in a table.
3. **Search Product** - search by ID or by name (case-insensitive, partial names work).
4. **Update Product Stock** - add stock or set an exact quantity.
5. **Process Customer Sale** - checks the product exists and stock is sufficient, calculates the total, deducts stock and prints a purchase summary.
6. **View Sales Records** - lists every completed sale.
7. **Generate Store Report** - totals, revenue, low-stock products (below 5), highest and lowest priced products.
8. **Exit**

## Data Structures
```python
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
]

sales_records = [
    {"id": 101, "name": "Milk", "quantity": 2, "total": 500.0}
]
```

## Python Concepts Used
- Lists and dictionaries (reading and updating values by key)
- Custom functions with parameters and `return`
- `while` loops for the menu and input validation, `for` loops for records
- `if / elif / else` for menu choices and sale checks
- `try / except ValueError` for input validation
- String methods (`.strip()`, `.title()`, `.lower()`, `.isdigit()`) and f-string formatting
- Built-ins: `len()`, `max()`, `min()`, `enumerate()`

## Main Functions
| Function | Purpose |
|---|---|
| `get_int()`, `get_price()`, `get_text()` | Validated user input |
| `find_product_by_id()` | Look up a product dictionary by ID |
| `add_product()` | Add a new product (no duplicate IDs) |
| `view_products()` | Display all products |
| `search_product()` | Find products by name or ID |
| `update_stock()` | Add to or set stock |
| `process_sale()` | Validate and complete a sale |
| `view_sales()` | Display sales records |
| `generate_report()` | Show store statistics |
| `main()` | Menu loop |

## How to Run
Requires Python 3.6 or newer.

```bash
git clone https://github.com/<your-username>/smart-grocery-store-system.git
cd smart-grocery-store-system
python grocery_store_system.py
```
(Use `python3` on macOS/Linux if needed.)

## Sample Input and Output

### Processing a sale
```text
--- Process Customer Sale ---
Enter product ID: 102
Enter quantity for Bread: 20
  Sale denied: only 14 units in stock.
...
Enter product ID: 102
Enter quantity for Bread: 6

  ----- Purchase Summary -----
  Product        : Bread
  Quantity       : 6
  Unit price     : Rs. 120.00
  Total amount   : Rs. 720.00
  Stock remaining: 8
```

### Viewing products
```text
ID      Name              Category           Price   Stock
----------------------------------------------------------
101     Milk              Dairy             250.00      20
102     Bread             Bakery            120.00       4
103     Rice              Grains            480.00      50
104     Sugar             Food              150.00      30
```

### Store report
```text
========================================
STORE REPORT
========================================
Total products          : 4
Total available stock   : 106
Total sales transactions: 2
Total revenue           : Rs. 1220.00

Products with stock below 5:
  None

Highest priced product(s):
  Rice - Rs. 480.00
Lowest priced product(s):
  Bread - Rs. 120.00
========================================
```

## Input Validation
- IDs, quantities and stock must be whole numbers; price must be greater than 0.
- Duplicate product IDs are blocked.
- Sales are refused for unknown products or when quantity exceeds stock.
- Invalid menu choices show a message and the menu repeats.

## Author
Your Name

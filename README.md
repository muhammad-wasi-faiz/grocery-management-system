# Smart Grocery Store Management System

## Overview
A console-based Python application that helps a local grocery store owner manage
products, stock, customer sales and reports. It uses **lists of dictionaries** as
its main data structures and runs from a menu until the user chooses to exit.

> **Important: data is not saved.** All products, stock levels and sales live in
> memory only. When you choose **8. Exit** (or close the terminal), everything you
> added or sold is **erased**, and the next run starts again from the three built-in
> sample products. See [Data Persistence and Limitations](#data-persistence-and-limitations).

## Repository Structure
```text
smart-grocery-store-system/
├── grocery_store_system.py        # the application
├── test_grocery_store_system.py   # automated tests (31 tests)
└── README.md
```

## Features
1. **Add New Product** - stores a product dictionary with `.append()`; duplicate IDs are rejected.
2. **View All Products** - shows ID, name, category, price and stock in a table.
3. **Search Product** - search by ID or by name (case-insensitive, partial names work).
4. **Update Product Stock** - add stock or set an exact quantity.
5. **Process Customer Sale** - checks the product exists and stock is sufficient, calculates the total, deducts stock and prints a purchase summary.
6. **View Sales Records** - lists every completed sale.
7. **Generate Store Report** - totals, revenue, low-stock products (below 5), highest and lowest priced products.
8. **Exit**

## Starting Data
Every run begins with these three products, and the sample output below starts from them:

| ID | Name | Category | Price | Stock |
|---|---|---|---|---|
| 101 | Milk | Dairy | 250 | 20 |
| 102 | Bread | Bakery | 120 | 4 |
| 103 | Rice | Grains | 480 | 50 |

## Data Structures
```python
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
]

sales_records = [
    {"id": 101, "name": "Milk", "quantity": 3, "total": 750.0}
]
```

## Python Concepts Used
- Lists and dictionaries (reading and updating values by key)
- Custom functions with parameters and `return`
- `while` loops for the menu and input validation, `for` loops for records
- `if / elif / else` for menu choices and sale checks
- `try / except ValueError` for input validation
- String methods (`.strip()`, `.title()`, `.lower()`, `.isdecimal()`) and f-string formatting
- Built-ins and modules: `len()`, `max()`, `min()`, `enumerate()`, `math.isfinite()`
- Automated testing with `unittest` and `unittest.mock`

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
Requires Python 3.6 or newer. No extra packages are needed.

1. Get the code: on this repository's GitHub page click the green **Code** button and either
   **Download ZIP** (then extract it) or copy the HTTPS link and run
   `git clone <the link you copied>`.
2. Open a terminal inside the `smart-grocery-store-system` folder.
3. Start the program:

```bash
python grocery_store_system.py
```
(Use `python3` instead of `python` on macOS/Linux if needed.)

## How to Run the Tests
From the same folder:

```bash
python -m unittest -v
```
All 31 tests should pass (`OK`). They feed scripted input to every menu operation and check the
printed output and the resulting data. They cover:

- the built-in starting stock (so the examples in this README cannot drift from the code),
- adding products, duplicate-ID rejection, and price validation,
- searching by name (partial and case-insensitive) and by ID,
- adding stock and setting exact stock,
- successful sales, sales denied for insufficient stock, unknown products, and selling exactly the remaining stock,
- the store report (with and without sales, tied prices, and an empty store),
- the menu's invalid-choice handling and the data-loss warning on exit.

## Sample Input and Output
All samples below come from a real run starting with the data in [Starting Data](#starting-data).

### Viewing products
```text
--- All Products ---
ID      Name              Category           Price   Stock
----------------------------------------------------------
101     Milk              Dairy             250.00      20
102     Bread             Bakery            120.00       4
103     Rice              Grains            480.00      50
```

### Processing a sale (one denied, one successful)
Bread starts with only 4 units, so asking for 5 is refused and nothing changes:
```text
--- Process Customer Sale ---
Enter product ID: 102
Enter quantity for Bread: 5
  Sale denied: only 4 units in stock.

--- Process Customer Sale ---
Enter product ID: 101
Enter quantity for Milk: 3

  ----- Purchase Summary -----
  Product        : Milk
  Quantity       : 3
  Unit price     : Rs. 250.00
  Total amount   : Rs. 750.00
  Stock remaining: 17
```

### Adding a product (invalid price rejected)
```text
--- Add New Product ---
Enter product ID: 104
Enter product name: sugar
Enter category: food
Enter price: inf
  Invalid price. Infinite or non-numeric values are not allowed.
Enter price: 150
Enter available stock: 30
  'Sugar' added successfully.
```

### Store report (after the steps above)
```text
STORE REPORT
Total products          : 4
Total available stock   : 101
Total sales transactions: 1
Total revenue           : Rs. 750.00

Products with stock below 5:
  Bread (ID 102) - 4 left

Highest priced product(s):
  Rice - Rs. 480.00
Lowest priced product(s):
  Bread - Rs. 120.00
```

### Exiting
```text
Note: products and sales are kept in memory only and are
erased when the program closes. Nothing is saved to disk.
Thank you for using the Smart Grocery Store System. Goodbye!
```

## Input Validation
- IDs, quantities and stock must be whole numbers (stock and quantity cannot be negative; sale quantity must be at least 1).
- Price must be a **finite** number greater than 0. Values such as `inf`, `-inf`, `nan` and `1e999`
  (which Python's `float()` would otherwise accept) are rejected.
- Duplicate product IDs are blocked.
- Sales are refused for unknown products or when the quantity exceeds the available stock.
- Searching with unusual characters (for example `²`) is handled safely and simply reports no match.
- Invalid menu choices show a message and the menu repeats.

## Data Persistence and Limitations
- **Data is lost when the program exits.** `products` and `sales_records` are ordinary Python lists
  held in RAM. Nothing is written to a file or database, so every product you add, every stock change
  and every sale disappears when the program closes. The next run resets to the three starting products.
- Because of this, **Sales Records and the Store Report only cover the current session.**
- To keep data between runs, a future version could save the two lists to a file (for example JSON or CSV)
  when the user exits and load them when the program starts.
- The program is single-user and runs in a terminal; there is no login or multi-user support.

## Author
Muhammad Wasi Faiz

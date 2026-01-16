# POS System for Small Cafes

#### Video Demo: <https://youtu.be/aNXoqI4ot1k?si=GPIwN432waNgviq8>

#### Description:

This is a simple yet functional **Point of Sale (POS) system** designed for small cafes, food stalls, or other retail setups that need a lightweight and offline solution. The system is written in Python and uses a CSV file to manage inventory data. It provides an interface for viewing available items, purchasing them, and automatically updating stock after each transaction.

The user is shown a list of products with prices and quantities in stock. They can then input the ID of the item they wish to purchase and the desired quantity. The system checks if enough stock is available and either completes the transaction or raises an error. After a successful transaction, the system updates the inventory in the CSV file.

This project also includes **unit tests** written with `pytest` to ensure key functions behave correctly. Errors such as selecting a non-existent item or ordering more than what's in stock are handled gracefully with informative error messages.

---

### Features:

- ✅ Load product inventory from `data/inventory.csv`
- ✅ Display a formatted list of items for sale
- ✅ Handle item purchase logic including stock updates
- ✅ Raise appropriate errors for invalid purchases (e.g., out of stock or invalid ID)
- ✅ Save updated inventory back to the CSV file
- ✅ Includes test cases for core functionalities using `pytest`

---

### File Breakdown:

- `project.py`:
  Contains all core functionality including:
  - `main()` – Starts the POS program
  - `load_inventory()` – Loads the inventory from CSV
  - `save_inventory()` – Writes updated inventory
  - `purchase_item()` – Handles purchase logic

- `test_project.py`:
  Includes tests for:
  - Successful purchase
  - Purchase with insufficient stock
  - Purchase with invalid item ID

- `data/inventory.csv`:
  Stores product data in this format:

```csv
id,name,price,stock
1,Coffee,3.5,12
2,Donut,1.25,47
3,Bagel,2.0,30

---

## Acknowledgments
I used ChatGPT for guidance but wrote and understand all the code myself which I have already explained in video

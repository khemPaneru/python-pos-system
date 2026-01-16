🛒 POS System for Small Cafes

🎥🎥 [Watch Video Demo](https://youtu.be/aNXoqI4ot1k)

📝 Description

This is a simple yet functional Point of Sale (POS) system for small cafes, food stalls, or other retail setups that need a lightweight offline solution. Written in Python, it uses a CSV file to manage inventory.

Users can:

View available items

Purchase items

Automatically update stock after each transaction

The system checks stock availability and raises clear errors for invalid inputs or insufficient stock.

✅ Includes unit tests using pytest to ensure all functions work correctly.

✨ Features

🗂 Load product inventory from data/inventory.csv

📋 Display a formatted list of items for sale

💰 Handle item purchase logic and stock updates

⚠️ Raise errors for invalid purchases (e.g., out of stock or invalid ID)

💾 Save updated inventory back to the CSV file

🧪 Unit tests for core functionalities

📁 File Breakdown

project.py – Main program logic:

main() – Starts the POS program

load_inventory() – Loads inventory from CSV

save_inventory() – Writes updated inventory

purchase_item() – Handles purchase logic

test_project.py – Unit tests for:

Successful purchase

Purchase with insufficient stock

Purchase with invalid item ID

data/inventory.csv – Inventory data format:

id,name,price,stock
1,Coffee,3.5,12
2,Donut,1.25,47
3,Bagel,2.0,30

🙏 Acknowledgments

Completed as part of CS50 Python course by Harvard University. All code was written and fully understood by me.
---

### 🙏 Special Thanks
Special thanks to **David J. Malan**, instructor of the CS50 Python course, for his guidance and teaching.

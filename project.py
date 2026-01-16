import csv
def load_inventory(filename="data/inventory.csv"):
    products = []

    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float( row["price"])
            row["stock"] = int(row["stock"])
            products.append(row)
    return products

def save_inventory(product_list, filename="data/inventory.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "stock"])
        writer.writeheader()
        for item in product_list:
            writer.writerow(item)


def purchase_item(products, item_id, quantity):
    for item in products:
        if item["id"] == item_id:
            if item["stock"] >= quantity:
                item["stock"] -= quantity
                return item["price"] * quantity
            else:
                raise ValueError("Not enough stock")
    raise ValueError("Item not found")

def main():
        inventory = load_inventory()
        print("Welcome to POS System")

        for item in inventory:
            print(f'{item["id"]}): {item["name"]} - ${item["price"]}  ({item["stock"]} in stock)')

        try:
            item_id = int(input("Enter item ID: "))
            quantity = int(input("Enter quantity: "))

            total = purchase_item(inventory, item_id, quantity)
            print(f"Total price: ${total}")

            save_inventory(inventory)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()


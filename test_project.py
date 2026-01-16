from project import purchase_item

def test_purchase_success():
    inventory = [
        {"id": 1, "name": "Coffee", "price": 3.5, "stock": 10}
    ]
    assert purchase_item(inventory, 1, 2) == 7.0
    assert inventory[0]["stock"] == 8

def test_purchase_insufficient_stock():
    inventory = [
        {"id": 2, "name": "Donut", "price": 1.25, "stock": 1}
    ]
    try:
        purchase_item(inventory, 2, 5)
    except ValueError as e:
        assert str(e) == "Not enough stock"

def test_purchase_invalid_id():
    inventory = [
        {"id": 3, "name": "Bagel", "price": 2.0, "stock": 3}
    ]
    try:
        purchase_item(inventory, 99, 1)
    except ValueError as e:
        assert str(e) == "Item not found"

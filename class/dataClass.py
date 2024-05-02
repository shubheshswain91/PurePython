from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand


items = InventoryItem("cheese", 2.5, 10)
print(items.unit_price)

print(items)
# prints InventoryItem(name='cheese', unit_price=2.5, quantity_on_hand=10)
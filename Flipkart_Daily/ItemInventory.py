frim Item import Item
class ItemInventory:
    def __init__(self):
        self.items = {}
        self.item_id = 1
    
    def add_item(self, brand, category, price, quantity):
        item = Item(self.item_id, brand, category, price, quantity)
        self.items[self.item_id] = item
        self.item_id+=1

    def get_item_by_id(self, item_id):
        return self.items[item_id] if self.item_exists(item_id) else None

    def item_exists(self, item_id):
        return item_id in self.items

    def check_quantity(self, item_id, quantity):
        item = self.items[item_id]
        return False if item.item_quantity < quantity else True

    def reduce_item_quantity(self, item_id, quantity):
        item = self.items[item_id]
        item.quantity -= quantity

    def increase_item_quantity(self, item_id, quantity):
        item = self.items[item_id]
        item.quantity += quantity



    
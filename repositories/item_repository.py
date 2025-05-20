# type: ignore
from models.item import Item

class ItemRepository:
    def __init__(self):
        self.items = {}
        self.counter = 1

    def create(self, name, description):
        item = Item(str(self.counter), name, description) 
        self.items[item.item_id] = item
        self.counter += 1
        return item
    
    def get_all(self):
        return [item.to_dict() for item in self.items.values()]
    
    def get_by_id(self, item_id):
        item = self.items.get(item_id)
        return item.to_dict() if item else None
    
    def update(self, item_id, name, description):
        if item_id in self.items:
            item = self.items.get(item_id)
            item.name = name
            item.description = description
            return item.to_dict()
        else:
            return None

    def delete(self, item_id):
        return self.items.pop(item_id, None) is not None    
    
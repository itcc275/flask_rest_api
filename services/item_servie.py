# type: ignore
from repositories.item_repository import ItemRepository

class ItemService:
    def __init__(self):
        self.repository = ItemRepository()

    def create_item(self, name, description):
        return self.repository.create(name, description) 
    
    def get_all_items(self):
        return self.repository.get_all()
    
    def get_item_by_id(self, item_id):
        return self.repository.get_by_id(item_id)
    
    def update_item(self, item_id, name, description):
        return self.repository.update(item_id, name, description)
    
    def delete_item(self, item_id):
        return self.repository.delete(item_id)
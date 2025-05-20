# type: ignore
class Item:
    def __init__(self, item_id, name, description):
        self.item_id = item_id
        self.name = name
        self.description = description

    def to_dict(self): 
        return {"id": self.item_id, "name": self.name, "description": self.description}
            
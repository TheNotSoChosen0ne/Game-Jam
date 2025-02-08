class Item():

    def __init__(self, name : str):
        self.name = name
        return

class Inventory():
    
    def __init__(self):
        self.storage = []
        return

    def addObject(self, object : Item):
        self.storage.append(object)
        return

    def size(self) -> int:
        return len(self.storage)

    def removeObject(self, object : Item):
        self.storage.remove(object)
        return

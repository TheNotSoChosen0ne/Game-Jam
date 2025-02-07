class Inventory():
    
    def __init__(self, name : str):
        self.name = name
        self.storage = []
        return

    def addObject(self, object):
        self.storage.append(object)
        return

    def size(self) -> int:
        return len(self.storage)

    def removeObject(self, object):
        self.storage.remove(object)
        return

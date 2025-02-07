class Clue():
    def __init__(self, name : str, type : str, findingMessage : str):
        self.find = False
        self.type = type
        self.name = name
        self.found_message = findingMessage
        return

    def found(self):
        print(self.found_message)
        self.find = True
        return

    def collect(self, inventory):
        inventory.addObject(self)
        print(self.name + " ajouté à : " + inventory.name)
        return

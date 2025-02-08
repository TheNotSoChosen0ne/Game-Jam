class Player():
    def __init__(self, name, position, inventory, sprite):
        self.position = position
        self.inventory = inventory
        self.sprite = sprite

    def set_pos(self, pos):
        self.position = pos
        return

import sprites

class Game():
    def __init__(self, text):
        self.text = text
        self.sprite = sprites.StaticSprite("../img/textbox.png", 0, 0)
        return

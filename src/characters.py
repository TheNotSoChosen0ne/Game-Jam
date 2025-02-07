class Character():
    def __init__(self, sex : str, name : str, job : str):
        self.name = name
        self.job = job
        self.sex = sex
        return

    def hello(self):
        print("Bonjour ! Je suis " + self.name + "(" + self.sex + ")" + " le " + self.job)
        return

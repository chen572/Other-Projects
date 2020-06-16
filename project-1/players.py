class Player:
    def __init__(self, name, money, record):
        self.name = name
        self.money = money
        self.record = record
    
    def __repr__(self):
        return self.name + " You have " + str(self.money) + "$"
    
    def update_money(self, amount):
        self.money += amount
        return self.money




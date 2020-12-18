import datetime


class Menu:
    def display(self):
        pass


class Game:
    def display(self):
        pass


class World:
    def __init__(self):
        self.time = datetime.datetime(year=0, month=0, day=1, hour=12, minute=0,
                                      second=0, microsecond=0, tzinfo=None)
        self.is_rainy = False
        # self.board = [20] * 100
        
    def set_weather(self, rainy=True):
        self.is_rainy = rainy


class Inventory:
    def __init__(self, size=[[False]*6]*4):
        self.size = size


class NPC:
    def __init__(self, name, pos, health, heigth=5, is_friendly=True, weight=55):
        self.name = name
        self.max_health = health
        self.health = health
        self.pos = pos
        self.heigth = heigth
        self.is_friendly = is_friendly
        self.weight = weight
    
    def set_health(self, health):
        self.health = health
    
    def change_health(self, health_change):
        if (self.health + health_change <= self.max_health) and (self.health + health_change >= 0):
            self.health = self.health + health_change
        elif self.health + health_change < 0:
            self.health = 0
        elif self.health + health_change > self.max_health:
            self.health = self.max_health
            

class Player:
    def __init__(self, player_name, pos, inventory=Inventory(), health=100, height=5, weight=50):
        self.name = player_name
        self.pos = pos
        self.health = health
        self.height = height
        self.weight = weight
        self.inventory = inventory


class Block:
    def __init__(self, name, width=1, height=1, is_stackable=True, is_placed=True):
        self.name = name
        self.size = (width, height)
        self.weight = 1
        self.is_stackable = is_stackable
        self.is_placed = is_placed
    
    def set_name(self, name):
        self.name = name


class Quest:
    def __init__(self, text, requester, condition, completed_text):
        self.text = text
        self.requester = requester
        self.condition = condition
        self.completed_text = completed_text
        self.completed = False
    
    def check_for_completed(self):
        if eval(self.condition):
            self.set_completed()
    
    def set_completed(self):
        self.completed = True

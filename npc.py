from spriteAnimations import *

def loadNPC():
    npc = {
            
    }

    return npc




class butcher():
    def __init__(self, name, x, y, itemsB, itemsE):
        self.name = name
        self.x = x
        self.y = y
        self.itemsB = itemsB
        self.itemsE = itemsE
        self.butcher = {
            "name":self.name,
            "stats": {
                "str":0,
                "dex":0,
                "int":0,
                "wis":0,
                "cha":0
            },
            "items":{
                "backpack":[self.itemsB],
                "equiped":[self.itemsE]
            },
            "HP":10,
            "maxHP":10,
            "sprite": loadButcher(),
            "X": self.x,
            "Y": self.y,
            "speed": 15,
            "image": 0,
            "animationSpeed": 250,
            "weightLimit": 15,
            "size":[67.5, 135],
            "spriteArray":{
                "walkR": [1, 4],
                "walkL": [5, 8],
                "walkU": [9, 12],
                "walkD": [13, 16],
                "standR": [17, 20],
                "standL": [21, 24],
                "standU": [25, 25],
                "standD": [26, 28]
            },
            "directionLooking": "down",
            "randomStandChance": [1, 20]
        }
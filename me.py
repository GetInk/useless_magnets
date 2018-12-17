from spriteAnimations import *

def loadMe():
    me = {
        "butcher": {
            "name":"Butcher",
            "stats": {
                "str":0,
                "dex":0,
                "int":0,
                "wis":0,
                "cha":0
            },
            "items":{
                "backpack":[],
                "equiped":[]
            },
            "HP":10,
            "maxHP":10,
            "sprite": loadButcher(),
            "X": 400,
            "Y": 400,
            "speed": 15,
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
        },
        "XP":{
            "XP":0,
            "perks":0,
        }
    }

    return me

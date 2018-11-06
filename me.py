from spriteAnimations import *

def loadMe():
    me = {
        "butcher": {
            "name":"Butcher",
            "stats": {
                "str":{
                    "name":"Str",
                    "count":0
                },
                "dex":{
                    "name":"Dex",
                    "count":0
                },
                "int":{
                    "name":"Int",
                    "count":0
                },
                "wis":{
                    "name":"Wis",
                    "count":0
                },
                "cha":{
                    "name":"Cha",
                    "count":0
                }
            },
            "items":{
                "backpack":[],
                "equiped":[]
            },
            "HP":0,
            "sprite": loadButcher(),
            "X": 400,
            "Y": 400,
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
        },
        "XP":{
            "XP":0,
            "perks":0,
        }
    }

    return me

npc = {
    "traveler":{
        "name":"traveler",
        "species":"human",
        "stats": {
            "str":{
                "name":"str",
                "count":1
            },
            "dex":{
                "name":"dex",
                "count":2
            },
            "int":{
                "name":"int",
                "count":3
            },
            "wis":{
                "name":"wis",
                "count":2
            },
            "cha":{
                "name":"cha",
                "count":0
            },
            "NV":{
                "name":"night vision",
                "count":False,
                "cause":None
            }
        },
        "items":{
            "backpack":{
                "lantern":{
                    "name":"lantern",
                    "count":1,
                    "damage":1,
                    "use":"str",
                    "lit":False
                },
                "dagger":{
                    "name":"dagger",
                    "count":2,
                    "damage":3,
                    "use":"dex"
                }
            },
            "equiped":{
                "light armor":{
                    "name":"leather armor",
                    "Dreduct":1
                }
            }
        },
        "dialogue":{
            "one":"hellow fellow traveler",
            "two":"pesky peseant!"
        },
        "HP":0,
        "XP":10
    }
}

for h in npc:
    npc[h]["HP"] = 10 + npc[h]["stats"]["str"]["count"]*2


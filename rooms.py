from colors import *


def loadRooms():
    rooms = {
        "doorConections":[["start", "room1", "door1"], ["start", "room2", "door2"], ["room1", "puzzleRoom", "door3"], ["room2", "puzzleRoom", "door4"], ["puzzleRoom", "keyRoom", "door5"], ["start", "hallway", "DOOR"]],
        "start":{
            "name":"PUZZLE ROOM",
            "items":[
                {
                    "block5":{
                        "name":"Block 5",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 30, gray, "squ"],
                        "whenDraw": 5
                    }
                },
                {
                    "block4":{
                        "name":"Block 4",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 60, cian, "squ"],
                        "whenDraw": 4
                    }
                },
                {
                    "block3":{
                        "name":"Block 3",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 90, blue, "squ"],
                        "whenDraw": 3
                    }
                },
                {
                    "block2":{
                        "name":"Block 2",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 120, purple, "squ"],
                        "whenDraw": 2
                    }
                },
                {
                    "block1":{
                        "name":"Block 1",
                        "type":"pedistalBlock",
                        "draw":[400, 400, 150, darkBlue, "squ"],    
                        "whenDraw": 1
                    }
                },
                {
                    "pedistal1":{
                        "name":"Pedistal 1",
                        "type":"pedistal",
                        "draw":[130, 400, 190, yellow, "squ"],
                        "whenDraw": 0,
                        "items":[],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "pedistal2":{
                        "name":"Pedistal 2",
                        "type":"pedistal",
                        "draw":[400, 400, 190, white, "squ"],
                        "whenDraw": 0,
                        "items":["block1", "block2", "block3", "block4", "block5"],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "pedistal3":{
                        "name":"Pedistal 3",
                        "type":"pedistal",
                        "draw":[670, 400, 190, yellow, "squ"],
                        "whenDraw": 0,
                        "items":[],
                        "pressure":True,
                        "pressed":False
                    }
                },
                {
                    "door1":{
                        "name":"Door 1",
                        "type":"door",
                        "draw":[15, 200, 30, 105, red, "rect"],
                        "whenDraw": 0,
                        "open": True,
                        "used": False
                }
                },
                    {
                    "door2":{
                        "name":"Door 2",
                        "type":"door",
                        "draw":[785, 200, 30, 105, red, "rect"],
                        "whenDraw": 0,
                        "open": True,
                        "used": False
                    }
                },
                {
                    "DOOR":{
                        "name":"Boss Door",
                        "type":"door",
                        "draw":[400, 20, 150, 40, red, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                }
            ],
            "message":[["SPACE TO PICK UP", cian, 0, 200, 50, False], ["LSHIFT TO DROP", cian, 0, 250, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "room1":{
            "name":"ROOM 1",
            "items":[
                {
                    "door1":{
                        "name":"Door 1",
                        "type":"door",
                        "draw":[785, 200, 30, 105, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False,
                    }
                },
                {
                    "magnet1":{
                        "name":"Magnet 1",
                        "type":"item",
                        "ability":"magnet",
                        "conected":"magnet2",
                        "direction":"",
                        "draw":[400, 400, 45, red, "squ"],
                        "whenDraw":6,
                        "weight":0
                    }
                },
                {
                    "door3":{
                        "name":"Door 3",
                        "type":"door",
                        "draw":[700, 785, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                }
            ],
            "message":[["INTERESTING ITEM", red, 0, -100, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "room2":{
            "name":"ROOM 2",
            "items":[
                {
                    "door2":{
                        "name":"Door 2",
                        "type":"door",
                        "draw":[15, 200, 30, 105, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False,
                    }
                },
                {
                    "magnet2":{
                        "name":"Magnet 2",
                        "type":"item",
                        "ability":"magnet",
                        "conected":"magnet1",
                        "direction":"",
                        "draw":[400, 400, 45, blue, "squ"],
                        "whenDraw":6,
                        "weight":0
                    }
                },
                {
                    "door4":{
                        "name":"Door 4",
                        "type":"door",
                        "draw":[100, 785, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                }
            ],
            "message":[["INTERESTING ITEM", red, 0, -100, 50, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "puzzleRoom":{
            "name":"PUZZLE ROOM",
            "items":[
                {
                    "door3":{
                        "name":"Door 3",
                        "type":"door",
                        "draw":[94, 15, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                },
                {
                    "door4":{
                        "name":"Door 4",
                        "type":"door",
                        "draw":[707, 15, 105, 30, green, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                },
                {
                    "wall1":{
                        "name":"Wall 1",
                        "type":"wall",
                        "draw":[200, 400, 25, 800, white, "rect"],
                        "whenDraw":0
                    }
                },
                {
                    "wall2":{
                        "name":"Wall 2",
                        "type":"wall",
                        "draw":[600, 400, 25, 800, white, "rect"],
                        "whenDraw":0
                    }
                },
                {
                    "pp":{
                        "name":"Pressure Plate",
                        "type":"itemPP",
                        "draw":[400, 400, 200, yellow, "squ"],
                        "pressed":False,
                        "whenDraw":0
                    }
                },
                {
                    "door5":{
                        "name":"door5",
                        "type":"door",
                        "draw":[400, 785, 105, 30, green, "rect"],
                        "open":True,
                        "used":False,
                        "whenDraw":0
                    }
                }
            ],
            "message":[],
            "npc":[],
            "background":[],
            "light":True
        },
        "keyRoom":{
            "name":"KEY ROOM",
            "items":[
                {
                    "door5":{
                        "name":"door5",
                        "type":"door",
                        "draw":[400, 15, 105, 30, green, "rect"],
                        "open":True,
                        "used":False,
                        "whenDraw":0
                    }
                },
                {
                    "key":{
                        "name":"Boss Door Key",
                        "type":"item",
                        "ability":"key",
                        "unlocks":"DOOR",
                        "weight":0,
                        "draw":[400, 400, 25, orange, "squ"],
                        "whenDraw":8
                    }
                }
            ],
            "message":[["BOSS DOOR KEY", yellow, 0, 100, 85, False]],
            "npc":[],
            "background":[],
            "light":True
        },
        "hallway":{
            "name":"HALLWAY OF DEATH",
            "items":[
                {
                    "DOOR":{
                        "name":"Boss Door",
                        "type":"door",
                        "draw":[400, 780, 150, 40, red, "rect"],
                        "whenDraw":0,
                        "open":True,
                        "used":False
                    }
                },
                {
                    "lava":{
                        "name":"lava",
                        "type":"decor",
                        "type2":"lava",
                        "lavaBubbles":[],
                        "draw":[150, 400, 300, 800, bloodRed, "rect"],
                        "whenDraw":-1
                    }
                },
                {
                    "lava2":{
                        "name":"lava",
                        "type":"decor",
                        "type2":"lava",
                        "lavaBubbles":[],
                        "draw":[650, 400, 300, 800, bloodRed, "rect"],
                        "whenDraw":-1
                    }
                },
                {
                    "projectile":{
                        "name":"rock",
                        "type":"projectile",
                        "direction":"left",
                        "speed":20,
                        "draw":[800, 400, 100, 20, white, "rect"],
                        "whenDraw":100
                    }
                },
                {
                    "projectile2":{
                        "name":"rock",
                        "type":"projectile",
                        "direction":"right",
                        "speed":15,
                        "draw":[0, 150, 100, 20, white, "rect"],
                        "whenDraw":100
                    }
                }
            ],
            "message":[["UNDER CONSTRUCTION", yellow, 0, -50, 60, True], ["KEEP OUT", yellow, 0, 50, 60, True]],
            "npc":[],
            "background":[],
            "light":True
        }
    }

    return rooms